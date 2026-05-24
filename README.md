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

## 🐳 Запуск через Docker

```bash
# Копируем .env
cp .env.template .env
# Заполни .env своими данными

# Запускаем все сервисы одной командой
docker compose up -d --build

# Создаём суперпользователя
docker compose exec web python manage.py createsuperuser

# Открываем в браузере
http://localhost/
http://localhost/swagger/

