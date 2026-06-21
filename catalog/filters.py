import django_filters

from catalog.models import Product


class ProductFilter(django_filters.FilterSet):
    """Фильтры для товаров."""

    price_min = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="gte",
    )

    price_max = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="lte",
    )

    class Meta:
        model = Product
        fields = {
            "category": ["exact"],
            "status": ["exact"],
            "is_custom": ["exact"],
            "is_author_project": ["exact"],
        }
