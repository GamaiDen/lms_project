# LMS Project

Платформа для онлайн-обучения на Django REST Framework.

## Функциональность
- CRUD для курсов (ViewSet)
- CRUD для уроков (Generic Views)
- Кастомная модель User (AbstractBaseUser, email)

## API Endpoints

### Курсы
- GET /api/courses/ — список курсов
- POST /api/courses/ — создать курс
- GET /api/courses/{id}/ — курс с уроками
- PUT /api/courses/{id}/ — обновить курс
- DELETE /api/courses/{id}/ — удалить курс

### Уроки
- GET /api/lessons/ — список уроков
- POST /api/lessons/ — создать урок
- GET /api/lessons/{id}/ — один урок
- PUT /api/lessons/{id}/ — обновить урок
- DELETE /api/lessons/{id}/ — удалить урок

## Установка
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## CI/CD

Проект использует GitHub Actions для автоматического тестирования и деплоя.

### Workflow:
1. **Test** — запуск тестов (PostgreSQL + Redis)
2. **Lint** — проверка кода flake8
3. **Deploy** — деплой на сервер (только для main)

### Secrets (нужно добавить в GitHub → Settings → Secrets):
- `SERVER_HOST` — IP сервера
- `SERVER_USER` — пользователь сервера
- `SSH_PRIVATE_KEY` — приватный SSH-ключ

### Ручной деплой:
```bash
ssh user@server
cd /opt/lms_project
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
sudo systemctl restart gunicorn

