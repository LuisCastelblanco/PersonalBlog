from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, register

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('register/', register, name='register'),
    path('', include(router.urls)), 
]