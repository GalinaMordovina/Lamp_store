from rest_framework import serializers

from orders.models import OrderRequest


class OrderRequestSerializer(serializers.ModelSerializer):
    """Сериализатор заявки клиента."""

    class Meta:
        model = OrderRequest
        fields = (
            "id",
            "request_type",
            "client_name",
            "contact",
            "product",
            "comment",
            "personal_data_agreement",
            "status",
            "created_at",
        )
        read_only_fields = (
            "id",
            "status",
            "created_at",
        )

    def validate_personal_data_agreement(self, value):
        """Проверяет согласие на обработку персональных данных."""

        if not value:
            raise serializers.ValidationError(
                "Необходимо согласие на обработку персональных данных."
            )

        return value
