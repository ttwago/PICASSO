# Тестовое задание
# Загрузка и обработка файлов (Django REST API с использованием Celery)

Этот проект представляет собой Django REST API, предназначенное для загрузки файлов на сервер и их асинхронной обработки с использованием Celery.

## Требования

- Python 3.x
- Django
- Django REST Framework
- Celery
- locust (доп. тесты)

## Установка и запуск

1. Клонируйте репозиторий:
   git clone https://github.com/ttwago/PICASSO.git

2. Перейдите в директорию проекта:
    cd ваш_проект

3. Установите зависимости из файла `requirements.txt`:
   pip install -r requirements.txt

4. Примените миграции:
   python manage.py migrate

5. Запустите сервер разработки:
    python manage.py runserver

6. Запустите Celery для асинхронной обработки задач:
   celery -A file_processing_project worker --loglevel=info

7. Cервер будет запущен по адресу http://localhost:8000/.


## Использование

1. Загрузка файла
    Чтобы загрузить файл на сервер, выполните POST-запрос на /api/upload/, включив файл в форме. Пример с использованием curl:

    curl -X POST -F "file=@путь_к_файлу" http://localhost:8000/api/upload/
    После успешной загрузки файла, вы получите статус 201 и данные файла.

2. Список файлов
    Для получения списка всех файлов и их статусов выполните GET-запрос на /api/files/.

3. Docker
    К сожалению, не сделал.

4. Тестирование
    Для тестирования проекта вы можете выполнить тесты, используя:

    python manage.py test

    Дополнительно, для тестирования нагрузки вы можете использовать locust.
    Установите его и запустите тесты

    pip install locust
    locust -f locustfile.py
