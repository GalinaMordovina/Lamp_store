from rest_framework import status
from rest_framework.test import APITestCase


class HealthCheckViewTest(APITestCase):
    """Тесты проверки работоспособности API."""

    def test_health_check_returns_ok(self):
        """Эндпоинт health должен возвращать статус ok."""

        response = self.client.get("/api/health/")

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"status": "ok"}
