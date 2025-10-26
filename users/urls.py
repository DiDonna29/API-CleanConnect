# users/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserProfileViewSet, CleanerProfileViewSet, HostProfileViewSet

router = DefaultRouter()

# Rutas para el usuario actual (usaremos 'me' para claridad)
router.register(r'users/me', UserProfileViewSet, basename='user-me')

# Rutas para perfiles (el usuario solo puede interactuar con el suyo)
router.register(r'profiles/cleaner', CleanerProfileViewSet, basename='cleaner-profile')
router.register(r'profiles/host', HostProfileViewSet, basename='host-profile')

urlpatterns = router.urls