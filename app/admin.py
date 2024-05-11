from django.contrib import admin
from . models import Product , Customer

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'locality', 'city', 'state', 'mobile', 'zipcode']
