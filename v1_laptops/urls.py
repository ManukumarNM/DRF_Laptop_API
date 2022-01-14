from django.urls import path
from v1_laptops import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('laptops/', views.laptop_list),
    path('laptops/<int:pk>/', views.laptop_detail),
]
# clean way of referring to a specific format
urlpatterns = format_suffix_patterns(urlpatterns)
