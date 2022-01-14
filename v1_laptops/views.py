# Writing Function Based Django views using our Serializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from v1_laptops.models import V1_Laptop
from v1_laptops.serializers import V1_LaptopSerializer



@api_view(['GET', 'POST'])   # The @api_view decorator for working with function based views.
def laptop_list(request, format=None): 

#Using format suffixes gives us URLs that explicitly refer to a given format, and means our API 
# will be able to handle URLs such as http://example.com/api/items/4.json.
    """
    List all code laptops, or create a new laptop.
    """
    if request.method == 'GET':
        laptops = V1_Laptop.objects.all()
        serializer = V1_LaptopSerializer(laptops, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = V1_LaptopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def laptop_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code laptop.
    """
    try:
        laptop = V1_Laptop.objects.get(pk=pk)
    except V1_Laptop.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = V1_LaptopSerializer(laptop)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = V1_LaptopSerializer(laptop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        laptop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)