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
Ветка 6: feature/catalog-api

#### English

Completed tasks:

* created serializers for categories, products and product images;
* implemented API endpoints for category and product catalog;
* added product detail endpoint;
* configured nested serialization for categories and images;
* added status display field (`status_display`);
* added parent category name field (`parent_name`);
* verified API operation through Django REST Framework interface.

Available endpoints:

* GET `/api/categories/`
* GET `/api/products/`
* GET `/api/products/<id>/`

Result:

The project now provides a REST API for catalog data. Products, categories and images can be consumed by frontend applications or external services.

---

#### Русский

Выполненные задачи:

* созданы сериализаторы для категорий, товаров и фотографий;
* реализованы API-эндпоинты каталога;
* добавлен эндпоинт детального просмотра товара;
* настроена вложенная сериализация категорий и фотографий;
* добавлено отображаемое название статуса (`status_display`);
* добавлено название родительской категории (`parent_name`);
* выполнена проверка работы API через интерфейс Django REST Framework.

Доступные эндпоинты:

* GET `/api/categories/`
* GET `/api/products/`
* GET `/api/products/<id>/`

Результат:

Проект получил полноценный REST API каталога товаров. Данные могут использоваться фронтендом, мобильным приложением или внешними сервисами.

