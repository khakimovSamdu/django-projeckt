from django.urls import path
from About_us.views import contact, developer, history
urlpatterns = [
    path('Contact/', contact),
    path('Developer/', developer),
    path('History/', history),
]
