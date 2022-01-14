from rest_framework import serializers
from v1_laptops.models import V1_Laptop, PROCESSOR_CHOICES, COLOR_CHOICES

#REST framework includes both Serializer classes, and ModelSerializer classes.

# # Create serializers using Serializer class
# class LaptopSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     brand = serializers.CharField(required=True, allow_blank=False, max_length=50)
#     model = serializers.CharField(max_length=50)
#     ssd = serializers.BooleanField(required=False)
#     processor = serializers.ChoiceField(choices=PROCESSOR_CHOICES, default='Corei3')
#     color = serializers.ChoiceField(choices=COLOR_CHOICES, default='Black')

#     def create(self, validated_data):
#         """
#         Create and return a new `Laptop` instance, given the validated data.
#         """
#         return Laptop.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Laptop` instance, given the validated data.
#         """
#         instance.brand = validated_data.get('brand', instance.brand)
#         instance.model = validated_data.get('model', instance.model)
#         instance.ssd = validated_data.get('ssd', instance.ssd)
#         instance.processor = validated_data.get('processor', instance.processor)
#         instance.color = validated_data.get('color', instance.color)
#         instance.save()
#         return instance


# Create serializers using Model Serializer
class V1_LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = V1_Laptop
        fields = ['id', 'brand', 'model', 'ssd', 'processor', 'color']

# ModelSerializer classes don't do anything particularly magical, they are simply a shortcut for creating serializer classes:
