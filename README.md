# Миграции

## Выполнено:

### Созданные файлы:

* [teacher_list.html](./templates/school/teacher_list.html)

* [settings_local.py](./website/settings_local.py)
---

### Измененные файлы:

* [students_list.html](./templates/school/students_list.html)

* [models.py](./school/models.py)

* [views.py](./school/views.py)

* [admin.py](./school/admin.py)

* [urls.py](./school/urls.py)
---


##Debug

####Применен Debug-Toolbar для определения количества SQL запросов: при применении метода prefetch_related количество запросов снижается.

##Запуск проекта

####Ддя запуска проекта необходимо записать в Settings.py переменную SECRET_KEY со значением отличным от пустого или
создать файл settings_local.py c той же переменной)


