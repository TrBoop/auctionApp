from http.client import HTTPResponse
from urllib import request, response
from django.contrib.auth import authenticate, login, views
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, Auction, Bid, Question, Answer
from .serializers import UserSerializer, AuctionSerializer, BidSerializer, QuestionSerializer, AnswerSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, SignupForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.contrib import auth
from django.contrib.auth.decorators import login_required


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
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

def signup_view(request):
    '''
    Signup function
    Users creating an account
    '''

    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            if not username:
                form.add_error('username', 'Please choose a username')
                return render(request, 'auth/signup.html', {'form': form})

            if CustomUser.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists')
                return render(request, 'auth/signup.html', {'form': form})

            if form.cleaned_data['password'] != form.cleaned_data['password_confirm']:
                form.add_error('password', 'Passwords to not match')
                form.add_error('password_confirm', 'Passwords to not match')
                return render(request, 'auth/signup.html', {'form': form})

            password = form.cleaned_data['password']
            userDateOfBirth = form.cleaned_data['userDateOfBirth']
            userEmail = form.cleaned_data['userEmail']
            # create a new user
            new_user = CustomUser.objects.create(username=username, userDateofBirth=userDateOfBirth, userEmail=userEmail)
            # set user's password
            new_user.set_password(password)
            new_user.save()
            # authenticate user
            # establishes a session, will add user object as attribute
            # on request objects, for all subsequent requests until logout
            user = auth.authenticate(username=username, password=password, )
            if user is not None:
                auth.login(request, user)
                return redirect('profile')

    return render(request, 'auth/signup.html', {'form': SignupForm})


def login_view(request):
    '''
    Login function
    Users logging into the app
    '''

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('profile')

            # failed authentication
            form.add_error('username', 'Invalid credentials')
            form.add_error('password', 'Invalid credentials')
            return render(request, 'auth/login.html', {'form': form})

    return render(request, 'auth/login.html', {'form': form})


@login_required
def logout_view(request):
    '''
    Once users logout they are redirected to login page
    '''

    auth.logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    '''
    A user's profile page
    Users can also use this view to update their profile text
    and image via the POST method
    '''

    user = request.user

    if 'text' in request.POST and request.POST['text']:
        text = request.POST['text'][:4096]
        if user.profile:
            user.profile.text = text
            user.profile.save()
        else:
            user.profile = Profile.objects.create(text=text)
            user.save()

        if 'profile_img' in request.FILES:
            user.profile.image = request.FILES['profile_img']
            user.profile.save()

    context = {
        'user': user,
        'page': 'profile',
        'profile': user.profile,
        'session_key': request.session.session_key,
        'meta': request.META,
    }

    return render(request, 'pages/profile.html', context)