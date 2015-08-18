testphoto
=========

# Установка
1. pip install -r requirements.txt

2.
CREATE DATABASE `testphoto` CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'testphoto'@'localhost' IDENTIFIED BY 'JJJxtymckjysqgfhjkm';
GRANT SELECT, INSERT, UPDATE, REFERENCES, DELETE, CREATE, DROP, ALTER, INDEX, TRIGGER, CREATE VIEW, SHOW VIEW, EXECUTE, ALTER ROUTINE, CREATE ROUTINE, CREATE TEMPORARY TABLES, LOCK TABLES, EVENT ON `testphoto`.* TO 'testphoto'@'';;
GRANT GRANT OPTION ON `testphoto`.* TO 'testphoto'@'';

2. python manage.py migrate

# Улучшения
1. Перенести state в таблицу tag для полноценного индексирования