from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse('''congo, created web application using django''')

def login(request):
    return render(request,'first.html')

def home(request):
    return render(request,'home.html')