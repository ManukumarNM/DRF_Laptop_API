from rest_framework import serializers
from v2_laptops.models import V2_Laptop, PROCESSOR_CHOICES, COLOR_CHOICES


# Create serializers using Model Serializer
class V2_LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = V2_Laptop
        fields = ['id', 'brand', 'model', 'ssd', 'processor', 'color']

# ModelSerializer classes don't do anything particularly magical, they 
# are simply a shortcut for creating serializer classes:
