from django.shortcuts import render
from .models import *
# Create your views here.
def category(request):
    product_item=Product.objects.all()
    return render(request,'category.html',{'products':product_item})