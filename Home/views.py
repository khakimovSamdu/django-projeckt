from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ab_history(request):
    return HttpResponse('Hello About -> History')
def ab_our_team(request):
    return HttpResponse('Hello About -> Our Team')
def pr_new_arrivals(request):
    return HttpResponse('Hello Products -> New Arrivals')
def pr_all_categories(request):
    return HttpResponse('Hello Products -> All Categories')
def pric_plan(request):
    return HttpResponse('Hello Pricing -> Plan Comparison')
def pric_available(request):
    return HttpResponse('Hello Pricing -> Available Plans')
def blog(request):
    return HttpResponse('Hello Blog')
def contact(request):
    return HttpResponse('Hello Contact')
