from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login_in(request):
    return HttpResponse('Hompage -> Account -> Login in')
def register(request):
    return HttpResponse('Homepage -> Account -> Register')
def profile(request):
    return HttpResponse('Homepage -> Account -> Profile')
