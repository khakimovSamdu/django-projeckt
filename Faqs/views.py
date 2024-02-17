from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def contact_us(request):
    return HttpResponse('Homepage -> FAQs -> Contact Us')
def message_form(request):
    return HttpResponse('Homepage -> FAQS -> Message Form')
def testimonial(request):
    return HttpResponse('Homepage -> FAQS -> Testimonial')
