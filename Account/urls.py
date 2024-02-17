from Account.views import login_in, register, profile
from django.urls import path
urlpatterns = [
    path('Login in/', login_in),
    path('Register', register),
    path('Profile', profile)
]