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
Ветка 2: feature/catalog-app

#### English

Completed tasks:

* created Django application `catalog`;
* connected the application to project settings;
* installed and configured Django REST Framework;
* created API endpoint `/api/health/`;
* implemented `HealthCheckView`;
* configured URL routing for the application;
* added the first automated API test;
* verified successful API response and project startup.

Result:

The project now contains a working REST API endpoint and a basic testing infrastructure for further backend development.

---

#### Русский

Выполненные задачи:

* создано приложение `catalog`;
* приложение подключено к настройкам проекта;
* установлен и настроен Django REST Framework;
* создан API-эндпоинт `/api/health/`;
* реализовано представление `HealthCheckView`;
* настроена маршрутизация приложения;
* добавлен первый автоматизированный тест API;
* проверена корректная работа API и запуск проекта.

Результат:

В проекте появилась базовая REST API-инфраструктура и подготовлена основа для дальнейшей разработки серверной части.
