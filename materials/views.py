from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer, CourseCreateSerializer
from users.permissions import IsModerator, IsOwner, IsNotModerator


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return CourseSerializer
        return CourseCreateSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsNotModerator()]
        elif self.action in ('update', 'partial_update', 'destroy'):
            return [IsAuthenticated(), IsModerator() | IsOwner()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsNotModerator()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH', 'DELETE'):
            return [IsAuthenticated(), IsModerator() | IsOwner()]
        return [IsAuthenticated()]
