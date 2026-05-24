# LMS Project

Платформа для онлайн-обучения на Django REST Framework.

## 🐳 Запуск через Docker

```bash
# Копируем .env
cp .env.template .env
# Заполни .env своими данными

# Запускаем все сервисы
docker compose up -d --build

# Создаём суперпользователя
docker compose exec web python manage.py createsuperuser

# Открываем в браузере
http://localhost/
http://localhost/swagger/

