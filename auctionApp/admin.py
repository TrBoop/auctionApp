from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Auction
from .models import Bid


admin.site.register(CustomUser)
admin.site.register(Auction)
admin.site.register(Bid)