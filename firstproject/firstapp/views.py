from django.shortcuts import render
from firstapp.models import Customer
from django.http import HttpResponse
from firstapp.form import CustomerForm
import pdfkit

# Create your views here.
def home1(request):
    x=CustomerForm()
    return render(request,'firstapp/base.html',{'form':x})
def customer1(request):
    cus1=request.POST['NAME']
    cus2=request.POST['MOBILE']
    cus3=request.POST['AGE']
    cus4=request.POST['CITY']
    f=Customer(NAME=cus1,MOBILE=cus2,AGE=cus3,CITY=cus4,)
    f.save()
    emp=Customer.objects.all()
    context={'emp':emp}
    return render(request,"firstapp/one.html",context)
def raju1(self):
       a=pdfkit.from_url('https://127.0.0.1:8000/abc/', 'customer.pdf')
       return render(a,content_type="application/pdf")
