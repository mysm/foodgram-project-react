 ## Продуктовый помощник - foodgram

 ![workflow](https://github.com/mysm/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

---

#### О проекте:
 Онлайн-сервис для хранения рецептов блюд и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
 
#### Технологии:
- Python
- Django
- Django REST Framework
- PostgreSQL
- Nginx
- Gunicorn
- Docker

#### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone <project>
cd foodgram-project-react/infra/
# сделайте копию файла <.env.example> в <.env>
cp .env .env
```

Установить Docker и Docker Compose:

```bash
sudo apt update
sudo apt install docker-ce docker-compose -y
```

Запуск контейнера:

```bash
docker-compose up -d
```

Инициализация базы:

```bash
sudo docker-compose exec backend python manage.py collectstatic --no-input
sudo docker-compose exec backend python manage.py makemigrations --noinput
sudo docker-compose exec backend python manage.py migrate --noinput
```

Заполнение базы данными:
```bash
# Для заполнения базы Тегами и ингредиентами выполните:
docker-compose exec backend python manage.py import_tags
docker-compose exec backend python manage.py import_ingredients
# Для заполнения базы пользователями и рецептами выполните:
docker-compose exec backend python manage.py data_test
```


Документация API:

`http://178.154.228.12/api/docs/redoc.html`

Проект:

`http://178.154.228.12`


Администратор:
`Логин: admin`
`email: mysm@mail.ru`
`Пароль: admin`
