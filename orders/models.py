from django.db import models

from catalog.models import Product


class OrderRequest(models.Model):
    """Заявка клиента на товар."""

    class RequestType(models.TextChoices):
        REQUEST = "request", "Оставить заявку"
        DISCUSS = "discuss", "Обсудить заказ"
        AVAILABILITY = "availability", "Уточнить наличие"
        SIMILAR = "similar", "Заказать похожее изделие"

    class Status(models.TextChoices):
        NEW = "new", "Новая"
        IN_PROGRESS = "in_progress", "В работе"
        DONE = "done", "Завершена"
        CANCELED = "canceled", "Отменена"

    request_type = models.CharField(
        max_length=20,
        choices=RequestType.choices,
        default=RequestType.REQUEST,
        verbose_name="Тип заявки",
    )
    client_name = models.CharField(
        max_length=100,
        verbose_name="Имя клиента",
    )
    contact = models.CharField(
        max_length=150,
        verbose_name="Контакт для связи",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="order_requests",
        verbose_name="Товар",
    )
    comment = models.TextField(
        blank=True,
        verbose_name="Комментарий",
    )
    personal_data_agreement = models.BooleanField(
        default=False,
        verbose_name="Согласие на обработку персональных данных",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
        verbose_name="Статус заявки",
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
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.client_name} — {self.product.name}"
