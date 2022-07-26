from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,db_constraint=False)
    name = models.CharField(max_length=200, null=True, help_text='Name....')
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='Product_images')
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    @property
    def ImageUrl(self):
        return self.image.url
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.customer.name
    @property
    def get_total_cart(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    @property
    def get_total_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
    
    
class OrderItem(models.Model):
				product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,db_constraint=False)
				order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True,db_constraint=False)
				quantity = models.IntegerField(default=0, null=True, blank=True)
				date_added = models.DateTimeField(auto_now_add=True)
				def __str__(self):
						return f"{self.order.customer} {self.product.name} ni oldi"
				@property
				def get_total(self):
					total=self.product.price * self.quantity
					return total
		

    
    
