from django.urls import path
from rest_framework import routers
from .views import UserViewSet
#routes the data to be viewed from the db
router = routers.DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls