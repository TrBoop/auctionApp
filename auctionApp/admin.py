from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Auction
from .models import Bid
from .models import Question
from .models import Answer


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Question)
admin.site.register(Answer)