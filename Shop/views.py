from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def categories(request):
    return HttpResponse('Homepage -> Shop -> Categories')
def product_det(request):
    return HttpResponse('Homepage -> Shop -> Product Detail')
def new_arrial(request):
    return HttpResponse('Homepage -> Shop -> New Arrival')
def compare_pr(request):
    return HttpResponse('Homepage -> Shop -> Compare Products')
def order_history(request):
    return HttpResponse('Homepage -> Shop -> Order History')
