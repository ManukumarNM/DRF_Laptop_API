# Writing GENERIC CLASS-BASED VIEWS

from v4_laptops.models import V4_Laptop
from v4_laptops.serializers import V4_LaptopSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions


class LaptopList(generics.ListCreateAPIView):
    queryset = V4_Laptop.objects.all()
    serializer_class = V4_LaptopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #Associating Laptops with Users
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LaptopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = V4_Laptop.objects.all()
    serializer_class = V4_LaptopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer