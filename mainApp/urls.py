from django.contrib import admin
from django.urls import path, include
#routes pages from main app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('auctionApp.urls'))
]
