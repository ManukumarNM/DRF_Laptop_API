# Writing regular Django views using our Serializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from laptops.models import Laptop
from laptops.serializers import LaptopSerializer

@csrf_exempt  #  we want to be able to POST to this view from clients that won't have a CSRF token we need to mark the view as csrf_exempt
def laptop_list(request):
    """
    List all code laptops, or create a new laptop.
    """
    if request.method == 'GET':
        laptops = Laptop.objects.all()
        serializer = LaptopSerializer(laptops, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LaptopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def laptop_detail(request, pk):
    """
    Retrieve, update or delete a code laptop.
    """
    try:
        laptop = Laptop.objects.get(pk=pk)
    except Laptop.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LaptopSerializer(laptop)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LaptopSerializer(laptop, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        laptop.delete()
        return HttpResponse(status=204)