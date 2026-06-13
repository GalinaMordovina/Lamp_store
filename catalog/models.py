from django.db import models


class Category(models.Model):
    """Категория товаров."""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="Родительская категория",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар."""

    class Status(models.TextChoices):          # пробую перечисление статусов через TextChoices
        AVAILABLE = "available", "В наличии"   # должно быть красиво
        CUSTOM = "custom", "Под заказ"
        SOLD = "sold", "Продано"
        ARCHIVE = "archive", "Архив"

    name = models.CharField(
        max_length=255,
        verbose_name="Название",
    )
    article = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Артикул",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,              # для товаров это лучше, чем CASCADE
        related_name="products",               # (если удалить категорию, то товары не исчезнут)
        verbose_name="Категория",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )
    specifications = models.TextField(
        blank=True,
        verbose_name="Характеристики",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
        verbose_name="Статус",
    )
    is_custom = models.BooleanField(
        default=False,
        verbose_name="Под заказ",
    )
    is_author_project = models.BooleanField(
        default=False,
        verbose_name="Авторский проект",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]

    def __str__(self):
        return self.name
