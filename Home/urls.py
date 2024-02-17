from django.urls import path
from Home.views import ab_history, ab_our_team, pr_new_arrivals, pr_all_categories, pric_plan, pric_available, blog, contact
urlpatterns = [
    path('About/History/', ab_history),
    path('About/Our Team/', ab_our_team),
    path('Products/New Arrivals/', pr_new_arrivals),
    path('Products/All Categories/', pr_all_categories),
    path('Pricing/Plan Comparison/', pric_plan),
    path('Pricing/Available Plans/', pric_available),
    path('Blog/', blog),
    path('Contact/', contact)
]