from http.client import HTTPResponse
from urllib import request, response
from django.contrib.auth import authenticate, login, views
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, Auction, Bid
from .serializers import UserSerializer, AuctionSerializer, BidSerializer, QuestionSerializer, AnswerSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm

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

def LoginView(request):
    authentication_form = AuthenticationForm
    username = request.POST['username']  
    password = request.POST['password']

    #create a post request with username and pw taken from request body, pass from vue app
    user = authenticate(username=username, password=password)
    #if user not null, use login function
    if user is not None:
        login(request, user)
        #redirect to main page
    return HTTPResponse()

    #access the session user as getUser()