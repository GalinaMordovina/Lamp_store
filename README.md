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
Ветка 6: feature/admin-inline-images

#### English

Completed tasks:

* implemented inline image management in Django Admin;
* added ProductImageInline to the product administration page;
* grouped product fields using fieldsets;
* improved product creation and editing workflow;
* enabled image management directly from the product page.

#### Result:

The administrative panel became more convenient for catalog management. Product information and images can now be managed from a single interface.

---

#### Русский

Выполненные задачи:

* реализовано встроенное управление фотографиями товаров через Django Admin;
* добавлен ProductImageInline в карточку товара;
* поля товара сгруппированы с использованием fieldsets;
* улучшен процесс создания и редактирования товаров;
* реализовано управление фотографиями непосредственно из карточки товара.

#### Результат:

Административная панель стала удобнее для наполнения каталога. Информация о товаре и его фотографии теперь управляются из одного интерфейса.
