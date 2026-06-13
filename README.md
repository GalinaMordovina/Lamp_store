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
Ветка 6: feature/postgresql-setup

#### English

Completed tasks:

* configured PostgreSQL database server;
* created a dedicated database for the project;
* created a dedicated database user;
* moved database connection settings to environment variables;
* configured Django to use PostgreSQL instead of SQLite;
* applied database migrations to PostgreSQL;
* created a new administrator account;
* verified successful operation of the project with PostgreSQL.

#### Result:

The project now uses PostgreSQL as the primary database management system and is prepared for further development and deployment.

---

#### Русский

Выполненные задачи:

* настроен сервер базы данных PostgreSQL;
* создана отдельная база данных проекта;
* создан отдельный пользователь базы данных;
* параметры подключения вынесены в переменные окружения;
* Django переведён с SQLite на PostgreSQL;
* выполнены миграции в PostgreSQL;
* создан новый суперпользователь;
* проверена корректная работа проекта с PostgreSQL.

#### Результат:

Проект переведён на PostgreSQL и подготовлен к дальнейшей разработке и будущему развёртыванию.
