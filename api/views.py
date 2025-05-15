from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer
from .permissions import IsOwnerOrReadOnly
from django.http import HttpResponse

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

def home(request):
    return HttpResponse("<h1>Welcome to My Django API 🚀</h1><p>Visit <a href='/api/v1/'>the API</a> or <a href='/api/schema/swagger-ui/'>API docs</a>.</p>")
