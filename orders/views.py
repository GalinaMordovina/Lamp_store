from rest_framework import generics
from rest_framework.permissions import AllowAny

from orders.models import OrderRequest
from orders.serializers import OrderRequestSerializer


class OrderRequestCreateView(generics.CreateAPIView):
    """Создание заявки клиента."""

    queryset = OrderRequest.objects.all()
    serializer_class = OrderRequestSerializer
    permission_classes = [AllowAny]
