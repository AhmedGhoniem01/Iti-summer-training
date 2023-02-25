from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"app1/home.html")
def contact(request):
    return render(request,"app1/contact.html")
def about(request):
    return render(request,"app1/about.html")






