from django.urls import path
from catalog.views import (
    CategoryListView,
    HealthCheckView,
    ProductDetailView,
    ProductListView,
)

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
