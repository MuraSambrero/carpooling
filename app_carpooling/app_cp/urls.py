from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, UserViewSet

router = DefaultRouter()
router.register('trips', TripViewSet, 'Trips')
router.register('users', UserViewSet, 'Users')

urlpatterns = [
    path('', include(router.urls)),
]