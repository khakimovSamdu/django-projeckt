from django.urls import path
from Support.views import faqs, support_form
urlpatterns = [
    path('FAQs/', faqs),
    path('Support form/', support_form)
]