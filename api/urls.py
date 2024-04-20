from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import MovieViewvSet, ActorViewSet, GenreViewSet , TechnicianViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewvSet)
router.register(r'actors', ActorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'technicians', TechnicianViewSet)


urlpatterns = [
    
    path('', include(router.urls))
]
