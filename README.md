﻿# Проект "Программа самообучения"

## Краткое описание

LMS-система, в которой пользователь-модератор может размещать материалы для самообразования, которые можно разделить на
секции. К материалам можно добавить тесты со своими вопросами. Каждый желающий после регистрации может изучать эти
материалы и проходить тесты.
Проект выполнен на Windows.
Создан с использованием Python и Django REST framework. Авторизация настроена с помощью JWT, настроен вывод документации
через Swagger. Управление всеми сущностями реализовано через Django Admin. В качестве базы данных используется
PostgreSQL.

## Инструкция по запуску

1. Создайте файл .env по образцу в файле .env.sample.
2. Установите зависимости проекта, указанные в файле pyproject.toml.
   ```bash
   poetry install
   ```
3. Выполните миграции
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
5. При необходимости загрузите тестовые данные с помощью фикстур или же внесите свои собственные данные.
   ```bash
   python manage.py loaddata learning_data.json
   python manage.py loaddata user_data.json
   ```

## Технологии в проекте (стек)

* Python 3.11
* Django
* DRF
* PostgreSQL
* JWT
* CORS
* Swagger
* Unittest
