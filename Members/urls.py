from django.urls import path
from Members.views import directory, become_a_member, membership
urlpatterns = [
    path('Directory/', directory),
    path('Become a member/', become_a_member),
    path('Membership/', membership),
]