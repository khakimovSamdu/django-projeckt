from django.urls import path 
from homeBlog.views import blogandnews, portofolio, profile, case_studies
urlpatterns = [
    path('Blog/Blog&News/', blogandnews),
    path('Blog/Portofolio/', portofolio),
    path('Blog/Profile/', profile),
    path('Blog/Case Studies/', case_studies)
]