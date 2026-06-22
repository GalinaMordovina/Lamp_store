from django.urls import path

from orders.views import OrderRequestCreateView


urlpatterns = [
    path("", OrderRequestCreateView.as_view(), name="order-request-create"),
]
