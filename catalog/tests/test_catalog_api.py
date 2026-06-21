import pytest
from rest_framework import status
from rest_framework.test import APIClient

from catalog.models import Category


@pytest.mark.django_db
def test_category_list_returns_categories():
    """Список категорий должен возвращать созданные категории."""

    client = APIClient()

    Category.objects.create(
        name="Освещение",
        description="Светильники, лампы и другое освещение.",
    )

    response = client.get("/api/categories/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Освещение"


@pytest.mark.django_db
def test_category_list_returns_empty_list():
    """Если категорий нет, должен вернуться пустой список."""

    client = APIClient()

    response = client.get("/api/categories/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []
