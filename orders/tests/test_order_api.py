import pytest
from rest_framework import status
from rest_framework.test import APIClient

from catalog.models import Category, Product
from orders.models import OrderRequest


@pytest.mark.django_db
def test_create_order_request_success():
    """Заявка должна успешно создаваться при наличии согласия."""

    client = APIClient()

    category = Category.objects.create(
        name="Освещение",
    )

    product = Product.objects.create(
        name='Светильник "Вишня"',
        article="LAMP-001",
        category=category,
        price=1500,
    )

    data = {
        "request_type": OrderRequest.RequestType.AVAILABILITY,
        "client_name": "Иванов Алексей",
        "contact": "vk.com/alex",
        "product": product.id,
        "comment": "Хочу уточнить наличие.",
        "personal_data_agreement": True,
    }

    response = client.post(
        "/api/orders/",
        data=data,
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert OrderRequest.objects.count() == 1

    order_request = OrderRequest.objects.first()

    assert order_request.client_name == "Иванов Алексей"
    assert order_request.status == OrderRequest.Status.NEW
    assert order_request.product == product


@pytest.mark.django_db
def test_create_order_request_without_agreement():
    """Заявка не должна создаваться без согласия на обработку данных."""

    client = APIClient()

    category = Category.objects.create(
        name="Освещение",
    )

    product = Product.objects.create(
        name='Светильник "Вишня"',
        article="LAMP-001",
        category=category,
        price=1500,
    )

    data = {
        "request_type": OrderRequest.RequestType.AVAILABILITY,
        "client_name": "Иванов Алексей",
        "contact": "vk.com/alex",
        "product": product.id,
        "comment": "Хочу уточнить наличие.",
        "personal_data_agreement": False,
    }

    response = client.post(
        "/api/orders/",
        data=data,
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert OrderRequest.objects.count() == 0

    assert "personal_data_agreement" in response.json()


@pytest.mark.django_db
def test_create_order_request_with_invalid_product():
    """Нельзя создать заявку для несуществующего товара."""

    client = APIClient()

    data = {
        "request_type": OrderRequest.RequestType.REQUEST,
        "client_name": "Иван Иванов",
        "contact": "vk.com/ivanov",
        "product": 9999,
        "comment": "Интересует товар.",
        "personal_data_agreement": True,
    }

    response = client.post(
        "/api/orders/",
        data=data,
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert OrderRequest.objects.count() == 0


@pytest.mark.django_db
def test_order_request_gets_default_status():
    """Новая заявка должна автоматически получать статус NEW."""

    client = APIClient()

    category = Category.objects.create(
        name="Освещение",
    )

    product = Product.objects.create(
        name='Светильник "Вишня"',
        article="LAMP-001",
        category=category,
        price=1500,
    )

    data = {
        "request_type": OrderRequest.RequestType.REQUEST,
        "client_name": "Иван Иванов",
        "contact": "vk.com/ivanov",
        "product": product.id,
        "comment": "",
        "personal_data_agreement": True,
    }

    response = client.post(
        "/api/orders/",
        data=data,
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED

    order_request = OrderRequest.objects.get()

    assert order_request.status == OrderRequest.Status.NEW


@pytest.mark.django_db
def test_create_order_request_without_client_name():
    """Нельзя создать заявку без имени клиента."""

    client = APIClient()

    category = Category.objects.create(
        name="Освещение",
    )

    product = Product.objects.create(
        name='Светильник "Вишня"',
        article="LAMP-001",
        category=category,
        price=1500,
    )

    data = {
        "request_type": OrderRequest.RequestType.REQUEST,
        "client_name": "",
        "contact": "vk.com/ivanov",
        "product": product.id,
        "comment": "",
        "personal_data_agreement": True,
    }

    response = client.post(
        "/api/orders/",
        data=data,
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert OrderRequest.objects.count() == 0
