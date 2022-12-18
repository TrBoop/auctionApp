from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
#routes pages from main app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('auctionApp.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('auth/', include('django.contrib.auth.urls')),
]
