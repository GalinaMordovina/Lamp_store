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
Ветка 1: feature/project-setup

### English

Completed tasks:

- initialized local Git repository;
- configured GitHub repository;
- created GitFlow workflow (`main`, `develop`, `feature/*`);
- configured `.gitignore`;
- created Python virtual environment;
- installed Django;
- installed project dependencies:
  - Django
  - python-dotenv
  - psycopg2-binary
- generated `requirements.txt`;
- initialized Django project (`config`);
- configured environment variables support;
- moved `SECRET_KEY` to `.env`;
- configured `DEBUG` and `ALLOWED_HOSTS` through environment variables.

### Result:

The project foundation has been prepared and Django is successfully running in the development environment.

### Русский

Выполненные задачи:

- инициализирован локальный Git-репозиторий;
- настроен репозиторий GitHub;
- организован GitFlow (`main`, `develop`, `feature/*`);
- настроен `.gitignore`;
- создано виртуальное окружение Python;
- установлен Django;
- установлены зависимости проекта: 
  - Django
  - python-dotenv
  - psycopg2-binary
- сформирован файл `requirements.txt`;
- создан Django-проект (`config`);
- настроена работа с переменными окружения;
- ключ `SECRET_KEY` вынесен в `.env`;
- параметры `DEBUG` и `ALLOWED_HOSTS` переведены на использование переменных окружения.

### Результат:

Подготовлена базовая инфраструктура проекта и успешно запущено Django-приложение в режиме разработки.