# LMS Project

Платформа для онлайн-обучения на Django REST Framework.

## Функциональность
- CRUD для курсов и уроков
- Пользователи и аутентификация (JWT)
- Подписки на курсы
- Платежи через Stripe
- Валидация видео-ссылок (YouTube)
- Пагинация
- Документация Swagger
- Celery + Celery Beat (фоновые задачи)
- Redis (кеширование + брокер)

## Запуск через Docker

```bash
# 1. Копируем .env
cp .env.template .env
# Заполни .env своими данными

# 2. Запускаем все сервисы
docker-compose up -d --build

# 3. Создаём суперпользователя
docker-compose exec web python manage.py createsuperuser

# 4. Открываем в браузере
http://localhost:8000/
http://localhost:8000/swagger/

