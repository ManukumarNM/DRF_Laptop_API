# Writing Class Based Django views using our Serializer

from v3_laptops.models import V3_Laptop
from v3_laptops.serializers import V3_LaptopSerializer
from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = V3_Laptop.objects.all()
    serializer_class = V3_LaptopSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = V3_Laptop.objects.all()
    serializer_class = V3_LaptopSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)