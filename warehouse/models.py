from django.db import models
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    customer = models.CharField(max_length=16, primary_key=True)
    customerName = models.CharField(max_length=64)
    address = models.CharField(max_length=1024)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    employeeID = models.ForeignKey(User, related_name="account_creator")
    createTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.customer

# when create a customer, create a customer account automatically at same time
class CustomerAccount(models.Model):
    customer = models.OneToOneField("Customer", auto_created=True, on_delete=models.CASCADE, primary_key=True)
    customerUserName = models.CharField(max_length=64, default="customer")
    customerPassword = models.CharField(max_length=128, default="666666")

    def __str__(self):
        return self.customerUserName

class Store(models.Model):
    store = models.CharField(max_length=16, primary_key=True)
    storeName = models.CharField(max_length=128)
    customerID = models.ForeignKey("Customer", related_name="store_owner", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.store

class Product(models.Model):
    product = models.CharField(max_length=16, primary_key=True)
    productName = models.CharField(max_length=128)
    # 店铺内展示商品数量
    productAmount = models.IntegerField(verbose_name="product_inventory", validators=[lambda x: x >= 0], default=0)
    # 商品所在的店铺
    store = models.ManyToManyField("Store")

    def __str__(self):
        return self.product

class ProductDetail(models.Model):
    product = models.OneToOneField("Product", auto_created=True, on_delete=models.CASCADE, primary_key=True, default=None)
    color = models.CharField(max_length=32)
    style = models.CharField(max_length=64)
    size = models.CharField(max_length=32)

# 订单
class Orders(models.Model):
    order = models.OneToOneField("EndUserOrder", auto_created=True)



# 上架的商品
'''
class StoreProduct(models.Model):
    storeID = models.ForeignKey(Store, on_delete=models.CASCADE, default=None, primary_key=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, primary_key=True)
'''

# 存放商品的仓库 客户将商品发到仓库保存便于发货
class Warehouse(models.Model):
    warehouse = models.CharField(max_length=16, primary_key=True)
    warehouseName = models.CharField(max_length=64)
    warehouseLocation = models.CharField(max_length=128)

# 商品放入warehouse的库存清单中
class Inventory(models.Model):
    inventory = models.CharField(max_length=16, primary_key=True)
    product = models.ForeignKey("Product")
    # 入库商品数量
    inventoryProductAmount = models.IntegerField(default=0)
    location = models.ForeignKey("Warehouse", to_field="warehouseLocation", related_name="product_inventory_location")

    def __str__(self):
        return self.inventory

# 当客户将订单发给 warehouse, warehouse 会处理相应的订单
# warehouse 将货物交由物流公司进行运输
class WarehouseOrders(models.Model):



# 终端用户
class EndUser(models.Model):
    user = models.CharField(max_length=16)
    userName = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

# 用户个人资料
class EndUserProfile(models.Model):
    user = models.OneToOneField("EndUser", primary_key=True)
    gender = models.BooleanField(default=True)
    birth = models.DateField(default=timezone.now)
    address = models.CharField(max_length=512, null=True)
    phone = models.CharField(max_length=11, validators=[MinLengthValidator(11)])


class EndUserOrders(models.Model):
    order = models.CharField(max_length=16, primary_key=True)
    # 下单的用户
    user = models.ForeignKey("EndUser")
    # 订单配送地址
    delivery_address = models.CharField(max_length=512)
    # 下单的商品
    product = models.ForeignKey("Product")

