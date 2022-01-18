"""API_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v_laptops/', include('laptops.urls')),
    path('v1_laptops/', include('v1_laptops.urls')),
    path('v2_laptops/', include('v2_laptops.urls')),
    path('v3_laptops/', include('v3_laptops.urls')),
    path('v4_laptops/', include('v4_laptops.urls')),

    path('api-auth/', include('rest_framework.urls')),
]
