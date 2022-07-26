from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import Customer, Order, OrderItem, Product, Category


class ProductUchun(admin.ModelAdmin):
    list_display = ['name','price','digital','image','description']
    list_per_page = 10
    ordering = ('name','price','digital','image','description')
admin.site.register(Product, ProductUchun)
    
    

class CustomerUchun(admin.ModelAdmin):
    list_display = ['user','name','email']
    list_per_page = 10
    ordering = ('user','name','email')
admin.site.register(Customer, CustomerUchun)   
    

class OrderUchun(admin.ModelAdmin):
    list_display = ['customer','date_ordered','complete','transaction_id']
    list_per_page = 10
    ordering = ('customer','date_ordered','complete','transaction_id')
admin.site.register(Order, OrderUchun)



class OrderItemUchun(admin.ModelAdmin):
    list_display = ['product','order','quantity','date_added']
    list_per_page = 10
    ordering = ('product','order','quantity','date_added')
admin.site.register(OrderItem, OrderItemUchun)
    

class CategoryUchun(admin.ModelAdmin):
    list_display = ['category_name']
    list_per_page = 10
    ordering = ('category_name')
admin.site.register(Category)