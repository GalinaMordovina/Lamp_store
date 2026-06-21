from django.contrib import admin

from orders.models import OrderRequest


@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    """Настройки отображения заявок в админке."""

    list_display = (
        "id",
        "client_name",
        "contact",
        "product",
        "request_type",
        "status",
        "personal_data_agreement",
        "created_at",
    )
    readonly_fields = (         # чтобы даты создания не редактировались вручную
        "created_at",
        "updated_at",
    )
    list_filter = (
        "request_type",
        "status",
        "personal_data_agreement",
        "created_at",
    )
    search_fields = (
        "client_name",
        "contact",
        "product__name",
        "comment",
    )
    ordering = (
        "-created_at",
    )
