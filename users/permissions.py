from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """Проверяет, является ли пользователь модератором."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модераторы').exists()


class IsOwner(BasePermission):
    """Проверяет, является ли пользователь владельцем объекта."""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsNotModerator(BasePermission):
    """Проверяет, что пользователь НЕ модератор."""

    def has_permission(self, request, view):
        return not request.user.groups.filter(name='Модераторы').exists()
