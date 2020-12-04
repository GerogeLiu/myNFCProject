from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^customerLogin/(?P<customerID>\d)$', views.customerLogin, name='customer_login'),
]