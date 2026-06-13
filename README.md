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
Ветка 5: feature/media-setup

#### English

Completed tasks:

* installed Pillow library;
* configured media file support;
* configured MEDIA_URL and MEDIA_ROOT;
* created ProductImage model;
* implemented support for multiple images per product;
* registered ProductImage model in Django admin;
* verified image upload through the administrative panel.

#### Result:

The project now supports product image storage and management. The catalog is prepared for displaying real workshop products.

---

#### Русский

Выполненные задачи:

* установлена библиотека Pillow;
* настроена работа с медиафайлами;
* настроены параметры MEDIA_URL и MEDIA_ROOT;
* создана модель ProductImage;
* реализована поддержка нескольких фотографий для одного товара;
* модель ProductImage зарегистрирована в административной панели;
* проверена загрузка изображений через административную панель.

#### Результат:

Проект получил поддержку хранения и управления фотографиями изделий. Каталог подготовлен для размещения реальных работ мастерской.
