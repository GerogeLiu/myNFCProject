from django.contrib import admin

from .models import Customer, CustomerAccount, Store, Product,\
    ProductDetail

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer", "customerName", "address", "phone", "email", "employeeID", "createTime")
    list_filter = ("customer", "customerName")
    search_fields = ("customer", "customerName")
    ordering = ['customer', 'customerName']


class CustomerAccountAdmin(admin.ModelAdmin):
    list_display = ("customerUserName", "customerPassword")


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerAccount, CustomerAccountAdmin)

admin.site.register(Store)
admin.site.register(Product)
admin.site.register(ProductDetail)
# admin.site.register(StoreProduct)
