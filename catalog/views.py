from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from catalog.models import Category, Product
from catalog.serializers import CategorySerializer, ProductSerializer
from catalog.filters import ProductFilter


class HealthCheckView(APIView):
    """Проверка работоспособности API."""

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response({"status": "ok"})


class CategoryListView(generics.ListAPIView):
    """Список категорий."""

    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    """Список товаров."""

    permission_classes = [AllowAny]
    queryset = Product.objects.select_related("category").prefetch_related("images")
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    search_fields = [
        "name",
        "article",
        "description",
        "specifications",
    ]

    ordering = ["name"]


class ProductDetailView(generics.RetrieveAPIView):
    """Детальная информация о товаре."""

    permission_classes = [AllowAny]
    queryset = Product.objects.select_related("category").prefetch_related("images")
    serializer_class = ProductSerializer
