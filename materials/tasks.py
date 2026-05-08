from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from users.models import Subscription


@shared_task
def send_course_update_email(course_id):
    """Отправляет письма подписчикам курса."""
    subscriptions = Subscription.objects.filter(course_id=course_id)
    emails = [sub.user.email for sub in subscriptions]

    if emails:
        send_mail(
            'Обновление курса',
            f'Курс был обновлён. Проверьте новые материалы!',
            'admin@lms.ru',
            emails,
            fail_silently=True,
        )
    return f'Отправлено {len(emails)} писем'


@shared_task
def check_last_login():
    """Блокирует пользователей, не заходивших более месяца."""
    from users.models import User
    month_ago = timezone.now() - timezone.timedelta(days=30)
    users = User.objects.filter(last_login__lt=month_ago, is_active=True)
    users.update(is_active=False)
    return f'Заблокировано {users.count()} пользователей'
