from rest_framework import serializers
from v4_laptops.models import V4_Laptop, PROCESSOR_CHOICES, COLOR_CHOICES
from django.contrib.auth.models import User


# Create serializers using Model Serializer
class V4_LaptopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = V4_Laptop
        fields = ['id', 'brand', 'model', 'ssd', 'processor', 'color', 'owner']

# ModelSerializer classes don't do anything particularly magical, they 
# are simply a shortcut for creating serializer classes:

class UserSerializer(serializers.ModelSerializer):
    #Because 'v4_laptops' is a reverse relationship on the User model
    #For more info for reverse relationship study django-tutorial
    v4_laptops = serializers.PrimaryKeyRelatedField(many=True, queryset=V4_Laptop.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'v4_laptops']
