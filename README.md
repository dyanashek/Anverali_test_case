# Different account for customers & freelancers
***
Сайт с регистрацией для заказчиков и исполнителей и django-админкой
## Функционал:
1. Регистрация
2. Авторизация
3. Отображение данных профиля
4. Админка

## Установка и использование:
- В директории anverali создайте .env, содержащий **DJANGO_KEY** django; и данные для подключения к PostgreSQL: **DB-name**, **USER_NAME**, **USER_PASSWORD**
- Создайте соответствующую БД в PostgreSQL
>  Подключение к PostgreSQL
```sh
psql -U username -h host -p port db_name
CREATE DATABASE db_name;
```
- Установить виртуальное окружение и активировать его (при необходимости):
> Установка и активация в корневой папке проекта
```sh
python3 -m venv venv
source venv/bin/activate # for macOS
source venv/Scripts/activate # for Windows
```
- Установить зависимости:
```sh
pip install -r requirements.txt
```
- Создать суперпользователя для подключения к админке (из директории, содержащей файл manage.py):
```sh
python3 manage.py createsuperuser
```
- Выполнить миграции (из директории, содержащей файл manage.py):
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
- Запустить проект (из директории, содержащей файл manage.py):
```sh
python3 manage.py runserver
```

