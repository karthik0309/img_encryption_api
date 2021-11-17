from .api_views import *
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewset, basename='users')


urlpatterns = router.urls