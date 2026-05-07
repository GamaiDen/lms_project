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
- **Celery + Celery Beat** (фоновые задачи)
- **Redis** (кеширование + брокер)

## Celery задачи
- `send_course_update_email` — рассылка подписчикам при обновлении курса
- `check_last_login` — блокировка пользователей, не входивших 30+ дней

## Запуск
```bash
# Сервер
python manage.py runserver

# Celery Worker
celery -A config worker -l info

# Celery Beat
celery -A config beat -l info

# Redis
redis-server

