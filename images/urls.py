from .api_views import *
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'images',ImagesViewset,basename='images')

urlpatterns = router.urls