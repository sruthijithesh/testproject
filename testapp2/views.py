from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Welcome to the site')

def customer(request):
    return render(request, 'customer.html')

def seller(request):
    return render(request, 'seller.html')