# ML-DL-Repository-Template
Шаблон репозитория для классического ML/DL проекта

**Задача:** Тут можно кратко описать задачу...

## Чтобы запустить проект локально:
1. Установите python 3.11 и выше
2. Склонировать репозиторий: ``git clone ...``
3. Создать виртуальное окружение: ``python -m venv venv``
4. Активироавть виртуальное окружение: ``venv\Scripts\activate`` (для windows)
5. Заполните ``.env`` файл:
6. Соберите проект: ``python setup.py``

```
S3_API_HOST=
S3_BUCKET_NAME=
S3_ACCESS_KEY=
S3_SECRET_KEY=

DVC_USE_SSL=True
DVC_REMOTE_URL=s3://ml-team-spb/businessguarantees
DVC_REMOTE_NAME=minio


MLFLOW_POSTGRES_DB=postgres_mlflow
MLFLOW_POSTGRES_USER=mlflow
MLFLOW_POSTGRES_PASSWORD=mlflow_password
MLFLOW_POSTGRES_PORT=5432
MLFLOW_POSTGRES_HOST=mlflow-postgres

# MLFLOW S3
BACKEND_STORE_URI=postgresql://${MLFLOW_POSTGRES_USER}:${MLFLOW_POSTGRES_PASSWORD}@localhost:${MLFLOW_POSTGRES_PORT}/${MLFLOW_POSTGRES_DB}
MLFLOW_TRACKING_URI=http://localhost:5000
MLFLOW_S3_ENDPOINT_URL=S3_API_HOST
MLFLOW_S3_REMOTE_URL=

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
MLFLOW_PORT=5000
```

## Чтобы запустить mlflow:
1. Получить доступ к докеру и настроить его
2. Заполнить env файл
3. Запустить mlflow (желательно в отдельной консоли): ``python mlflow/mlflow_start.py``

## Принцип ведения git:

Во время разработки следует следует создавать новые ветки из ``main``.

1. Чтобы добавить новый функционал, создаем ветку ``название_нового_функционала`` от ``main``.

(Хочу добавить поддержку линейной регрессии -> название ветки: ``add: linear_reg_support``)

2. Чтобы пофиксить баг создаем ветку ``fix: описание_бага`` от ``main``

(Хочу добавить пофиксить баг подключение к БД -> название ветки: ``fix: bd_connection``)

3. Чтобы что-то инициализировать ``init: описание``

## Полезные git команды:
1. ``git checkout -b branch_name`` - создать ветку и переключиться на нее
2. ``git branch`` - отобразить все существующие ветки
3. ``git push -u origin new branch``  - отправить новую ветку в удаленный репозиторий
4. ``git reset -soft HEAD~1`` - удалить последний 1 коммит, но сохранить изменения
5. ``git branch -d <branch-name>`` - удалить ветку из локального репозиторию
6. ``git checkout current_branch`` ``->`` ``git merge target_branch`` – подтянуть изменения из ``target_branch`` ветки в ``current_branch``
7. ``git checkout --track -b local_branch_name origin/remote_branch_name`` – Чтобы склонировать конкретную существующую в удаленном репозитории ветку, нужно ввести команду
8. ``git rm --cached filename`` (если директория, то ``-r filename``) – удалить что-то из всевидящего GIT - ока:

## Полезные команды Poetry:
1. ``poetry update`` - обновить зависимость по pyproject.toml файлу
2. ``poetry install`` - установить все зависимости по pyproject.toml и poetry.lock файлам
3. ``poetry add --group group_name lib_name`` - добавить библиотеку в зависимости (``--group group_name`` - не обязательно)
4. ``poetry remove lib_name`` - удалить библиотеку из зависимостей
5. ``poetry run pre-commit run --all-files`` - запустить pre-commit хуки

## Полезные команды DVC:
1. ``dvc init`` - инициализировать все dvc файлы
2. ``dvc add path/to/...`` - добавить в dvc папку/файл
3. ``dvc commit`` - Фиксирует изменения
4. ``dvc push `` - загрузить измененные данные в s3
5. ``dvc pull`` - выгрузить данные из s3
6. ``dvc remote list`` - показать список доступных хранилищ
7. ``dvc diff`` - показать разницу между предыдущими версиями
8. ``dvc checkout`` - восстановить данные из предыдущего коммита

## Полезные команды Docker:
1. ``docker-compose down -v`` - (удалить контейнеры, включая volumes)
2. ``docker-compose down`` - (удалить контейнеры)
3. ``docker-compose build --no-cache`` - пересобрать, не используя кэш
4. ``docker-compose build`` - пересобрать
5. ``docker-compose up -d`` - запустить в detouch моде (логи не отображаются в консоли)
6. ``docker-compose up -d --build`` - запустить в detouch моде и пересобрать
7. ``docker ps`` - вывести список запущенных контейнеров

## Полезные команды:
1. ``set PYTHONPATH=%PYTHONPATH%;C:\Users\<username>\PycharmProjects\`` - перед запуском jupyter notebook. Чтобы корректно работали во вложенных папках, а не только в корне (для PyCharm)
2. Установить прокси совкомбанка:
    - ``set http_proxy=http://proxy-server``
    - ``set https_proxy=http://proxy-server``
    - ``set no_proxylocalhost,127.0.0.1,192.168.*,10.60.*``
