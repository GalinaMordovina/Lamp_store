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
Ветка 11: feature/orders

#### English

Completed tasks:

* created `orders` application;
* added `OrderRequest` model;
* added request type choices:

  * leave a request;
  * discuss an order;
  * check availability;
  * order a similar product;
* added request status choices;
* added customer contact fields;
* added personal data agreement field;
* connected order requests with products;
* created and applied database migrations;
* registered order requests in Django Admin;
* verified manual order request creation through the admin panel.

#### Result:

The project now supports customer order requests. Requests can be created, stored in PostgreSQL and managed through the administrative panel.

---

#### Русский

Выполненные задачи:

* создано приложение `orders`;
* добавлена модель `OrderRequest`;
* добавлены типы заявок:

  * оставить заявку;
  * обсудить заказ;
  * уточнить наличие;
  * заказать похожее изделие;
* добавлены статусы заявок;
* добавлены поля контактных данных клиента;
* добавлено поле согласия на обработку персональных данных;
* настроена связь заявки с товаром;
* созданы и применены миграции базы данных;
* заявки зарегистрированы в административной панели Django;
* проверено ручное создание заявки через админку.

#### Результат:

В проект добавлена система клиентских заявок. Заявки сохраняются в PostgreSQL и могут управляться через административную панель.
