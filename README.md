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
Ветка 10: feature/catalog-api-tests

#### English

Completed tasks:

* configured pytest and pytest-django;
* added API tests for health check endpoint;
* added tests for category API;
* added tests for product API;
* added tests for product detail endpoint;
* added tests for filtering functionality;
* added tests for product search;
* configured PostgreSQL test database support.

Implemented tests:

* health check endpoint;
* category list;
* empty category list;
* product list;
* empty product list;
* product detail;
* product not found (404);
* filtering by status;
* filtering by category;
* filtering by minimum price;
* product search by name.

Result:

The project now includes automated API testing with pytest and pytest-django. Core catalog functionality is covered by tests.

---

#### Русский

Выполненные задачи:

* настроены pytest и pytest-django;
* добавлены тесты для эндпоинта проверки работоспособности API;
* добавлены тесты API категорий;
* добавлены тесты API товаров;
* добавлены тесты детального просмотра товара;
* добавлены тесты фильтрации товаров;
* добавлены тесты поиска товаров;
* настроена работа тестов с PostgreSQL.

Реализованные тесты:

* проверка health endpoint;
* список категорий;
* пустой список категорий;
* список товаров;
* пустой список товаров;
* детальная карточка товара;
* возврат ошибки 404;
* фильтрация по статусу;
* фильтрация по категории;
* фильтрация по минимальной цене;
* поиск товара по названию.

Результат:

В проекте настроено автоматизированное тестирование API с использованием pytest и pytest-django. Основная функциональность каталога покрыта тестами.
