from django.urls import path
from Services.views import order_summary, shipping_method, return_plicy, payment_method, write_rev
urlpatterns = [
    path('Services/Order Summary/', order_summary),
    path('Services/Shipping Method', shipping_method),
    path('Services/Return Policy/', return_plicy),
    path('Services/Payment Method', payment_method),
    path('Services/Write Review/', write_rev)
]