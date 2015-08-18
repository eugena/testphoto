testphoto
=========

# Установка

Установка пакетов (нужен pip):

```bash
pip install -r requirements.txt
```
Создание базы данных:

```sql
CREATE DATABASE `testphoto` CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE USER 'testphoto'@'localhost' IDENTIFIED BY 'JJJxtymckjysqgfhjkm';

GRANT SELECT, INSERT, UPDATE, REFERENCES, DELETE, CREATE, DROP, ALTER, INDEX, TRIGGER, CREATE VIEW, SHOW VIEW, EXECUTE, ALTER ROUTINE, CREATE ROUTINE, CREATE TEMPORARY TABLES, LOCK TABLES, EVENT ON `testphoto`.* TO 'testphoto'@'';;

GRANT GRANT OPTION ON `testphoto`.* TO 'testphoto'@'';
```

Запуск миграции:

```bash
python manage.py migrate
```

Загрузка данных:

```bash
python manage.py loaddata fixtures/initial_data.yml
```

Запуск сайта:

```bash
python manage.py runserver
```
или через сокет.


# Улучшения
1. Перенести state в таблицу tag для полноценного индексирования.