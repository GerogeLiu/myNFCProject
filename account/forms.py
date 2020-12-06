from django import forms
from warehouse.models import CustomerAccount

class CustomerLoginForm(forms.Form):
    customerId = forms.CharField()
    customerId.widget.attrs['readonly'] = True
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)




class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)