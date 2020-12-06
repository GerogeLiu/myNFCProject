from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^customerlogin/(?P<customerId>\w*)$', views.customer_login, name="customer_login"),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^checkcode.html$', views.getcheck_code),
]