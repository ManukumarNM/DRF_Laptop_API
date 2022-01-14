from django.urls import path
from v3_laptops import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('laptops/', views.LaptopList.as_view()),
    path('laptops/<int:pk>/', views.LaptopDetail.as_view()),
]
# clean way of referring to a specific format
urlpatterns = format_suffix_patterns(urlpatterns)

