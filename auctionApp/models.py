from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
import random
from django.contrib.auth.models import UserManager

class CustomUser(AbstractUser):

#resource used to construct model: https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project

    userPassword = models.CharField(max_length=40)
    username = models.CharField(max_length=40, unique = True, primary_key=True)
    userEmail = models.EmailField(max_length = 254, unique = True)
    userDateOfBirth = models.DateField(max_length=8)

    #images in a model: https://stackoverflow.com/questions/6396442/add-image-avatar-field-to-users
    userImage = models.ImageField(upload_to='images', default = './images/defaultProf.png')

    USERNAME_FIELD = 'userEmail'
    REQUIRED_FIELDS = ['username', 'userDateOfBirth']

    objects = UserManager()


    """ Returns object name """
    def __str__(self):
        return self.username

    """ Converts the variables to dictionary """
    def to_dict(self):
        return {
            'id' : self.id,
            'username': self.username,
            'password': self.userPassword,
            'email' : self.userEmail,
            'image' :self.userImage,
            'DateOfBirth' : self.userDateOfBirth,
        }
        
    #orders db entries by email address and names the table User
    class Meta:
        ordering = ["userEmail"]
        verbose_name = "User"

class Auction(models.Model):
    itemTitle = models.CharField(max_length=255)
    itemDescription = models.CharField(max_length=255)
    itemStartPrice = models.IntegerField()
    itemPicture = models.ImageField()
    itemFinishDate = models.DateField('Finish Date')
    ownerId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.itemTitle

    def to_dict(self):
        return {
            'id' : self.id,
            'title' : self.itemTitle,
            'description' : self.itemDescription,
            'starting' : self.itemStartPrice,
            'picture' : self.itemPicture,
            'finish' : self.itemFinishDate,
            'owner' : self.ownerId,
        }


class Bid(models.Model):
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bidAmount = models.IntegerField()
    auctionId = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def to_dict(self):
        return {
            'id' : self.id,
            'bidder' : self.userId,
            'amount' : self.bidAmount,
            'item' : self.auctionId,
        }

class Question(models.Model):
    auctionId = models.ForeignKey(Auction, on_delete=models.CASCADE)
    questionText = models.CharField(max_length=255)
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def to_dict(self):
        return {
            'id' : self.id,
            'user' : self.userId,
            'question' : self.questionText,
            'item' : self.auctionId,
        }

class Answer(models.Model):
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerText = models.CharField(max_length=255)
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def to_dict(self):
        return {
            'id' : self.id,
            'user' : self.userId,
            'answer' : self.answerText,
            'question' : self.questionId,
        }
