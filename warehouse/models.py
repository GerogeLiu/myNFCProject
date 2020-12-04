from django.db import models
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    customerID = models.CharField(max_length=16, primary_key=True)
    customerName = models.CharField(max_length=64)
    address = models.CharField(max_length=1024)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    employeeID = models.ForeignKey(User, related_name="account_creator")
    createTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.customerID

# when create a customer, create a customer account automatically at same time
class CustomerAccount(models.Model):
    customerID = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    customerUserName = models.CharField(max_length=64, default="customer")
    customerPassword = models.CharField(max_length=128, default="666666")

    def __str__(self):
        return self.customerUserName

class Store(models.Model):
    storeID = models.CharField(max_length=16, primary_key=True)
    storeName = models.CharField(max_length=128)
    customerID = models.ForeignKey(Customer, related_name="store_owner", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.storeID

class Product(models.Model):
    productID = models.CharField(max_length=16, primary_key=True)
    productName = models.CharField(max_length=128)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.productID

class ProductDetail(models.Model):
    productID = models.OneToOneField(Product, on_delete=models.CASCADE, default=None, primary_key=True)
    color = models.CharField(max_length=32)
    style = models.CharField(max_length=64)
    size = models.CharField(max_length=32)

    def __str__(self):
        return "productID: " + self.productID + "productDetailID: " + self.productDetailID

class StoreProduct(models.Model):
    storeID = models.OneToOneField(Store, on_delete=models.CASCADE, default=None, primary_key=True)
    productID = models.OneToOneField(Product, on_delete=models.CASCADE, default=None, primary_key=True)

    def __str__(self):
        return self.storeProductID

