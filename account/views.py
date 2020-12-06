from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import CustomerLoginForm, UserLoginForm
from io import BytesIO

from . import tools
# Create your views here.

def getcheck_code(request):
    code = tools.getCheckChar()
    img = tools.getImg(code)
    f = BytesIO()
    img.save(f, 'PNG')
    request.session['check_code']=code
    # print(f.getvalue())
    return HttpResponse(f.getvalue())

# customer login
def customer_login(request, customerId):
    if request.method == 'POST':
        login_form = CustomerLoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            customer = authenticate(username=cd['username'], password=cd['password'])

            if customer:
                login(request, customer)
                return HttpResponse("Welcome You. You have been authenticated successfully")
            else:
                return HttpResponse("Sorry, Your username or password is not right")
        else:
            return HttpResponse("Invalid login")

    if request.method == 'GET':
        login_form = CustomerLoginForm()
        login_form.fields['customerId'].initial = customerId
        return render(request, "account/customer_login.html", {"form": login_form, "customerId": customerId})

# end user login
def user_login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return HttpResponse("Welcome You. You have been authenticated successfully")
            else:
                print("check_code: " + request.session['check_code'])
                return HttpResponse("Sorry, Your username or password is not right")
        else:
            return HttpResponse("Invalid login")

    if request.method == 'GET':
        login_form = UserLoginForm()
        return render(request, "account/user_login.html", {"form": login_form})