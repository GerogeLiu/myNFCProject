from django.shortcuts import render
from .models import Customer, CustomerAccount

# Create your views here.
def index(request):
    customers = Customer.objects.all()
    return render(request, "warehouse/index.html", {'customers': customers})

def customerLogin(request, customerID):
    # customer = CustomerAccount.objects.get(id=customerID)
    return render(request, "warehouse/customerLogin.html", {"customer": customerID})
