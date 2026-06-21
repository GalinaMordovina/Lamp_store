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
Ветка 6: feature/product-filtering

#### English

Completed tasks:

* installed and configured `django-filter`;
* added product filtering support;
* created `ProductFilter`;
* added filtering by category;
* added filtering by product status;
* added filtering by custom order flag;
* added filtering by author project flag;
* added filtering by minimum and maximum price;
* added product search by name, article, description and specifications;
* made catalog API endpoints publicly available for viewing.

Available query parameters:

* `category`
* `status`
* `is_custom`
* `is_author_project`
* `price_min`
* `price_max`
* `search`

Examples:

* GET `/api/products/?category=2`
* GET `/api/products/?status=available`
* GET `/api/products/?price_min=1000`
* GET `/api/products/?price_max=5000`
* GET `/api/products/?search=вишня`

Result:

The catalog API now supports filtering and search, making product browsing more flexible and closer to a real online store experience.

---

#### Русский

Выполненные задачи:

* установлен и настроен пакет `django-filter`;
* добавлена поддержка фильтрации товаров;
* создан фильтр `ProductFilter`;
* добавлена фильтрация по категории;
* добавлена фильтрация по статусу товара;
* добавлена фильтрация по признаку изделия под заказ;
* добавлена фильтрация по признаку авторского проекта;
* добавлена фильтрация по минимальной и максимальной цене;
* добавлен поиск товаров по названию, артикулу, описанию и характеристикам;
* API каталога сделан публично доступным для просмотра.

Доступные query-параметры:

* `category`
* `status`
* `is_custom`
* `is_author_project`
* `price_min`
* `price_max`
* `search`

Примеры:

* GET `/api/products/?category=2`
* GET `/api/products/?status=available`
* GET `/api/products/?price_min=1000`
* GET `/api/products/?price_max=5000`
* GET `/api/products/?search=вишня`

Результат:

API каталога получил поддержку фильтрации и поиска товаров. Просмотр каталога стал гибче и ближе к функциональности реального интернет-магазина.
