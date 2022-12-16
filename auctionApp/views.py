from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, Auction, Bid
from .serializers import UserSerializer, AuctionSerializer, BidSerializer, QuestionSerializer, AnswerSerializer
#Serializes data from db
class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
     
class AuctionViewSet(ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
     
class BidViewSet(ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

class QuestionViewSet(ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = AnswerSerializer