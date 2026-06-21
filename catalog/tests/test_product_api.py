import pytest
from rest_framework import status
from rest_framework.test import APIClient

from catalog.models import Category, Product


@pytest.mark.django_db
def test_product_list_returns_products():
    """Список товаров должен возвращать созданные товары."""

    client = APIClient()

    category = Category.objects.create(
        name="Освещение",
    )

    Product.objects.create(
        name="Светильник Вишня",
        article="LAMP-001",
        category=category,
        price=1500,
    )

    response = client.get("/api/products/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Светильник Вишня"


@pytest.mark.django_db
def test_product_list_returns_empty_list():
    """Если товаров нет, должен вернуться пустой список."""

    client = APIClient()

    response = client.get("/api/products/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


@pytest.mark.django_db
def test_product_detail_returns_product():
    """Детальная информация о товаре должна возвращаться корректно."""

    client = APIClient()

    category = Category.objects.create(
        name="Освещение",
    )

    product = Product.objects.create(
        name="Светильник Вишня",
        article="LAMP-001",
        category=category,
        price=1500,
    )

    response = client.get(f"/api/products/{product.id}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "Светильник Вишня"
    assert response.json()["article"] == "LAMP-001"


@pytest.mark.django_db
def test_product_detail_returns_404():
    """Несуществующий товар должен возвращать 404."""

    client = APIClient()

    response = client.get("/api/products/9999/")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_product_filter_by_status():
    """Список товаров должен фильтроваться по статусу."""

    client = APIClient()

    category = Category.objects.create(name="Освещение")

    Product.objects.create(
        name="Светильник Вишня",
        article="LAMP-001",
        category=category,
        price=1500,
        status=Product.Status.AVAILABLE,
    )

    Product.objects.create(
        name="Светильник Яблоня",
        article="LAMP-002",
        category=category,
        price=2000,
        status=Product.Status.CUSTOM,
    )

    response = client.get("/api/products/?status=available")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Светильник Вишня"


@pytest.mark.django_db
def test_product_search_by_name():
    """Список товаров должен поддерживать поиск по названию."""

    client = APIClient()

    category = Category.objects.create(name="Освещение")

    Product.objects.create(
        name="Светильник Вишня",
        article="LAMP-001",
        category=category,
        price=1500,
    )

    Product.objects.create(
        name="Светильник Яблоня",
        article="LAMP-002",
        category=category,
        price=2000,
    )

    response = client.get("/api/products/?search=вишня")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Светильник Вишня"


@pytest.mark.django_db
def test_product_filter_by_category():
    """Список товаров должен фильтроваться по категории."""

    client = APIClient()

    lighting = Category.objects.create(
        name="Освещение",
    )

    furniture = Category.objects.create(
        name="Мебель",
    )

    Product.objects.create(
        name="Светильник Вишня",
        article="LAMP-001",
        category=lighting,
        price=1500,
    )

    Product.objects.create(
        name="Стол Дуб",
        article="TABLE-001",
        category=furniture,
        price=5000,
    )

    response = client.get(
        f"/api/products/?category={lighting.id}"
    )

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Светильник Вишня"


@pytest.mark.django_db
def test_product_filter_by_min_price():
    """Список товаров должен фильтроваться по минимальной цене."""

    client = APIClient()

    category = Category.objects.create(
        name="Освещение",
    )

    Product.objects.create(
        name="Светильник Вишня",
        article="LAMP-001",
        category=category,
        price=1500,
    )

    Product.objects.create(
        name="Светильник Яблоня",
        article="LAMP-002",
        category=category,
        price=500,
    )

    response = client.get(
        "/api/products/?price_min=1000"
    )

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Светильник Вишня"
