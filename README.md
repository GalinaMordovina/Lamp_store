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
Ветка 3: feature/product-models

#### English

Completed tasks:

- created `Category` model;
- added support for nested categories;
- created `Product` model;
- added product statuses;
- added product article field;
- configured category and product relations;
- created and applied database migrations;
- registered models in Django admin panel;
- verified model display in admin panel.

Result: The project now contains the main catalog models and is ready for further product management development.

---

#### Русский

Выполненные задачи:

- создана модель `Category`;
- добавлена поддержка вложенных категорий;
- создана модель `Product`;
- добавлены статусы товаров;
- добавлено поле артикула товара;
- настроена связь товара с категорией;
- созданы и применены миграции базы данных;
- модели зарегистрированы в административной панели Django;
- проверено отображение моделей в админке.

Результат: В проекте появились основные модели каталога. Проект готов к дальнейшей разработке управления товарами.