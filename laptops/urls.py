from django.urls import path
from laptops import views

urlpatterns = [
    path('laptops/', views.laptop_list),
    path('laptops/<int:pk>/', views.laptop_detail),
]