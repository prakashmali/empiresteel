from django.shortcuts import render
from . models import Product
# Create your views here.

def index(request):
    obj=Product.objects.all()
    context={
            'data':obj
            }
    return render(request,'index.html',context)
