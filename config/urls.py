from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from materials.views import CourseViewSet, LessonListCreateView, LessonRetrieveUpdateDestroyView

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('api/lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-detail'),
]
