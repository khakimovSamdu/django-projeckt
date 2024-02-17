from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def order_summary(request):
    return HttpResponse('Homepage -> Services -> Order Summary')
def shipping_method(request):
    return HttpResponse('Homepage -> Services -> Shipping Method')
def return_plicy(request):
    return HttpResponse('Homepage -> Services -> Return Policy')
def payment_method(request):
    return HttpResponse('Homepage -> Services -> Payment Method')
def write_rev(request):
    return HttpResponse('Homepage -> Services -> Write Review')
