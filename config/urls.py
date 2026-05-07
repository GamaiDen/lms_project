from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from materials.views import CourseViewSet, LessonListCreateView, LessonRetrieveUpdateDestroyView
from users.views import UserProfileView, UserRegisterView, PaymentListView, SubscriptionView, PaymentCreateView

schema_view = get_schema_view(
    openapi.Info(
        title="LMS API",
        default_version='v1',
        description="API для платформы обучения",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('api/lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-detail'),
    path('api/users/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('api/users/register/', UserRegisterView.as_view(), name='user-register'),
    path('api/payments/', PaymentListView.as_view(), name='payment-list'),
    path('api/payments/create/', PaymentCreateView.as_view(), name='payment-create'),
    path('api/subscription/', SubscriptionView.as_view(), name='subscription'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
