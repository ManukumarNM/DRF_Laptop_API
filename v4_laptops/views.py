# Writing GENERIC CLASS-BASED VIEWS

from v4_laptops.models import V4_Laptop
from v4_laptops.serializers import V4_LaptopSerializer
from rest_framework import generics


class LaptopList(generics.ListCreateAPIView):
    queryset = V4_Laptop.objects.all()
    serializer_class = V4_LaptopSerializer


class LaptopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = V4_Laptop.objects.all()
    serializer_class = V4_LaptopSerializer

    