from django.urls import path
from Shop.views import categories, product_det, new_arrial, compare_pr, order_history
urlpatterns = [
    path('Shop/Categories/', categories),
    path('Shop/Product Detail/', product_det),
    path('Shop/New Arrival/', new_arrial),
    path('Shop/Compare Products/', compare_pr),
    path('Shop/Order History/', order_history)
]