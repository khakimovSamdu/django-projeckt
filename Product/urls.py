from django.urls import path
from Product.views import free_trial, features, case_students, solutions

urlpatterns = [
    path('Free_trial/', free_trial),
    path('Features/', features),
    path('Case_students/', case_students),
    path('Solutions/', solutions)
]