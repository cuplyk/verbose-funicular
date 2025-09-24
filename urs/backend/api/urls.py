from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import health_check

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('accounts.urls')),
    path('health/', health_check, name='health-check'),
]