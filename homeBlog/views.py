from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blogandnews(request):
    return HttpResponse('Homepage -> Blog -> Blog & News')
def portofolio(request):
    return HttpResponse('Homepage -> Blog -> Portofolio')
def profile(request):
    return HttpResponse('Hompage -> Blog -> Profile')
def case_studies(request):
    return HttpResponse('Homepage -> Blog -> Case Studies')

