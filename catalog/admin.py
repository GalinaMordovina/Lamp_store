from django.contrib import admin

from catalog.models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройки отображения категорий в админке."""

    list_display = ("id", "name", "parent", "created_at")
    list_filter = ("parent",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Настройки отображения товаров в админке."""

    list_display = (
        "id",
        "name",
        "article",
        "category",
        "price",
        "status",
        "is_custom",
        "is_author_project",
        "created_at",
    )
    list_filter = (
        "category",
        "status",
        "is_custom",
        "is_author_project",
    )
    search_fields = ("name", "article", "description", "specifications")
    ordering = ("name",)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    """Настройки отображения фотографий товаров в админке."""

    list_display = (
        "id",
        "product",
        "is_main",
        "created_at",
    )
    list_filter = (
        "is_main",
    )
    search_fields = (
        "product__name",
        "product__article",
    )
    ordering = (
        "-created_at",
    )
