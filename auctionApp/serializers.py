from rest_framework import serializers 
from auctionApp.models import CustomUser, Auction, Bid
 
 
class UserSerializer(serializers.ModelSerializer):
#creates a dictionary for the data in our db 
    class Meta:
        model = CustomUser
        fields = ['password',
                  'username',
                  'userEmail',
                  'userDateOfBirth',
                  'userImage'] 

class AuctionSerializer(serializers.ModelSerializer):
#creates a dictionary for the data in our db 
    class Meta:
        model = Auction
        fields = ['id',
                  'itemTitle',
                  'itemDescription',
                  'itemStartPrice',
                  'itemPicture',
                  'itemFinishDate',
                  'ownerId'] 

class BidSerializer(serializers.ModelSerializer):
#creates a dictionary for the data in our db 
    class Meta:
        model = Bid
        fields = ['id',
                #need to change later
                  'userId',
                  'bidAmount',
                  'auctionId'] 