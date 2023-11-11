from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','category','selling_price','discount_price', 'description',]
