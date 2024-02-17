from django.urls import path
from Faqs.views import contact_us, message_form, testimonial
urlpatterns = [
    path('FAQS/Contact Us/',contact_us),
    path('FAQS/Message From/', message_form),
    path('FAQS/Testimonial', testimonial)
]