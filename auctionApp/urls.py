from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, AuctionViewSet, BidViewSet
#routes the data to be viewed from the db
router = routers.DefaultRouter()
path('users/', include('django.contrib.auth.urls')),
router.register('users', UserViewSet,include('django.contrib.auth.urls'))
router.register('auction',AuctionViewSet)
router.register('bid',BidViewSet)

urlpatterns = router.urls
urlpatterns+=[path('users/', include('django.contrib.auth.urls')),]