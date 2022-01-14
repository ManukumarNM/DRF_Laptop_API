from rest_framework import serializers
from v4_laptops.models import V4_Laptop, PROCESSOR_CHOICES, COLOR_CHOICES


# Create serializers using Model Serializer
class V4_LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = V4_Laptop
        fields = ['id', 'brand', 'model', 'ssd', 'processor', 'color']

# ModelSerializer classes don't do anything particularly magical, they 
# are simply a shortcut for creating serializer classes:
