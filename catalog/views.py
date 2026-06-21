from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.models import Category, Product
from catalog.serializers import CategorySerializer, ProductSerializer


class HealthCheckView(APIView):
    """Проверка работоспособности API."""

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response({"status": "ok"})


class CategoryListView(generics.ListAPIView):
    """Список категорий."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    """Список товаров."""

    queryset = Product.objects.select_related("category").prefetch_related("images")
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    """Детальная информация о товаре."""

    queryset = Product.objects.select_related("category").prefetch_related("images")
    serializer_class = ProductSerializer
