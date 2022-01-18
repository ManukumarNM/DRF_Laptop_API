from django.urls import path
from v4_laptops import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('laptops/', views.LaptopList.as_view()),
    path('laptops/<int:pk>/', views.LaptopDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
# clean way of referring to a specific format
urlpatterns = format_suffix_patterns(urlpatterns)

