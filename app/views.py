from django.shortcuts import render
from django.views import View
from .models import Product
from django.db.models import Count
from . forms import CustomerRegisterForms
from django.contrib import messages
def home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Service(request):
    return render(request,'service.html')

class Category(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title= Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request,'category.html',locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product=Product.objects.filter(title=val)
        title= Product.objects.filter(category=product[0].category).values('title')
        return render(request,'category.html',locals())
    
class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'productdetail.html',locals())
    
class CustomerRegisterViews(View):
    def get(self, request):
        form=CustomerRegisterForms()
        return render(request,'customeregister.html',locals())
    def post(self, request):
        form=CustomerRegisterForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations user register')
        else:
            messages.warning(request,'Invalid Input Data')
        return render(request,'customeregister.html',locals())
    
from .forms import ProfileForms   
class ProfileView(View):
    def get(self, request):
        return render(request,'profile.html',locals())
    def post(self, request):
        form = ProfileForms(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            # Redirect or do something else
        else:
            form = ProfileForms()
        return render(request,'profile.html',locals())
        
        
        