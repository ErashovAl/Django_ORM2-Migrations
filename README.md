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


## Debug

#### Применен Debug-Toolbar для определения количества SQL запросов: при применении метода prefetch_related количество запросов снижается.

## Запуск проекта

#### Ддя запуска проекта необходимо записать в settings_local.py значение секретного ключа (любое).

#### З.Ы. Кроме списка [учеников](http://127.0.0.1:8000/) можно посмотреть список [учителей](http://127.0.0.1:8000/teacher/)
