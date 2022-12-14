from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Auction

admin.site.register(CustomUser)
admin.site.register(Auction)