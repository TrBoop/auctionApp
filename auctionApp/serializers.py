from rest_framework import serializers 
from auctionApp.models import CustomUser
 
 
class UserSerializer(serializers.ModelSerializer):
#creates a dictionary for the data in our db 
    class Meta:
        model = CustomUser
        fields = ['id',
                  'userPassword',
                  'username',
                  'userEmail',
                  'userDateOfBirth',
                  'userImage'] 