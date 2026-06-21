from rest_framework import serializers

from catalog.models import Category, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    """Сериализатор фотографий товара."""

    class Meta:
        model = ProductImage
        fields = (
            "id",
            "image",
            "is_main",
        )


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категорий."""

    parent_name = serializers.CharField(
        source="parent.name",
        read_only=True,
    )

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "description",
            "parent",
            "parent_name",
        )


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор товаров."""

    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    status_display = serializers.CharField(
        source="get_status_display",
        read_only=True,
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "article",
            "category",
            "description",
            "specifications",
            "price",
            "status",
            "status_display",
            "is_custom",
            "is_author_project",
            "images",
        )
