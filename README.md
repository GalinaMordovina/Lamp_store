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
Ветка 13: feature/order-api-tests

#### English

Completed tasks:

* created a dedicated test structure for the orders application;
* added API tests for order request creation;
* added validation tests for personal data agreement;
* added validation tests for product existence;
* added validation tests for required customer fields;
* verified automatic status assignment for new requests.

Implemented tests:

* successful order request creation;
* request creation without personal data agreement;
* request creation with invalid product identifier;
* automatic assignment of status `new`;
* request creation without customer name.

#### Result:

The order request API is covered by automated tests. Core business rules and validation scenarios are verified using pytest and pytest-django.

---

#### Русский

Выполненные задачи:

* создана отдельная структура тестов для приложения orders;
* добавлены тесты API создания заявок;
* добавлены тесты проверки согласия на обработку персональных данных;
* добавлены тесты проверки существования товара;
* добавлены тесты проверки обязательных полей клиента;
* проверено автоматическое назначение статуса новой заявки.

Реализованные тесты:

* успешное создание заявки;
* создание заявки без согласия на обработку персональных данных;
* создание заявки с несуществующим товаром;
* автоматическое назначение статуса `new`;
* создание заявки без имени клиента.

#### Результат:

API клиентских заявок покрыт автоматизированными тестами. Проверены основные бизнес-правила и сценарии валидации с использованием pytest и pytest-django.
