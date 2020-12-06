from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^customerLogin/(?P<customerID>\w*)$', views.customerLogin, name='customer_login'),
]