from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from .api_views import *

router = DefaultRouter()

router.register(r'images',ImagesViewset,basename='images')

urlpatterns = router.urls