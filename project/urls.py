from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Support/', include('Support.urls')),
    path('Product/', include('Product.urls')),
    path('Members/', include('Members.urls')),
    # path('Blog/', include('Blog.urls')),
    path('About us/', include('About_us.urls')),
    path('Home/', include('Home.urls')),

    # Homepage api manzil
    path('ACCOUNT/', include('Account.urls')),
    path('Homepage2/', include('homeBlog.urls')),
    path('Homepage3/', include('Faqs.urls')),
    path('Homepage4/', include('Services.urls')),
    path('Homepage5/', include('Shop.urls')),

]
