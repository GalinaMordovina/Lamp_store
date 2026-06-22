# Lamp Store

## Description

Lamp Store is a Django-based web catalog for handmade lamps and 3D models.

Users can:

* view products;
* open product detail pages;
* send order requests;
* contact the author through a request form or social links.

The website does not include online payment. Orders are discussed individually after the request is submitted.

## Описание

Lamp Store - это веб-каталог авторских ламп и 3D-моделей на Django.

Пользователи смогут:

* просматривать товары;
* открывать карточки изделий;
* отправлять заявки на заказ;
* связываться с автором через форму заявки или социальные сети.

На сайте не будет онлайн-оплаты. Заказы обсуждаются индивидуально после отправки заявки.



## Development History
Ветка 12: feature/order-api

#### English

Completed tasks:

* created API endpoint for customer order requests;
* implemented serializer for `OrderRequest`;
* configured validation of personal data agreement;
* implemented request creation through Django REST Framework;
* connected order API URLs;
* configured public access for request creation;
* tested API through DRF interface.

Implemented endpoint:

* `POST /api/orders/`

Validation:

* customer must provide personal data processing agreement;
* request status is assigned automatically;
* creation date is assigned automatically.

#### Result:

Customers can now submit order requests directly through the API. Submitted requests are stored in PostgreSQL and become available in the administrative panel for further processing.

---

#### Русский

Выполненные задачи:

* создан API-эндпоинт для клиентских заявок;
* реализован сериализатор `OrderRequest`;
* настроена валидация согласия на обработку персональных данных;
* реализовано создание заявок через Django REST Framework;
* подключены маршруты API заявок;
* настроен публичный доступ к созданию заявок;
* проведено тестирование через интерфейс DRF.

Реализованный эндпоинт:

* `POST /api/orders/`

Валидация:

* клиент обязан подтвердить согласие на обработку персональных данных;
* статус заявки назначается автоматически;
* дата создания заполняется автоматически.

#### Результат:

Пользователь может отправить заявку непосредственно через API. Заявка сохраняется в PostgreSQL и становится доступной для обработки через административную панель.
