from django.urls import path, include, re_path
from rest_framework import routers 
from .views import UserViewSet, AuctionViewSet, BidViewSet
#routes the data to be viewed from the db
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('auction',AuctionViewSet)
router.register('bid',BidViewSet)
urlpatterns = router.urls