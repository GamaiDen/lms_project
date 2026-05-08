from rest_framework import serializers


class URLValidator:
    """Валидатор для проверки, что ссылка ведёт на youtube.com."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = value.get(self.field, '')
        if url and 'youtube.com' not in url:
            raise serializers.ValidationError(f'{self.field}: ссылка должна быть на youtube.com')
