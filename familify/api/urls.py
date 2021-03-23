from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToMorseViewSet, ToTextViewSet

# Create a router and register our viewsets within it
router = DefaultRouter()
router.register(r'2text', ToTextViewSet, basename='2text')
router.register(r'2morse', ToMorseViewSet, basename='2morse')


# the API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]


