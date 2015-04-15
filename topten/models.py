import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class FlickrUser(models.Model):
    username = models.CharField(max_length = 200)
    user_id = models.CharField(max_length = 200)
    def __str__(self):
    	return self.username
    	
class Photo(models.Model):
	photo_id = models.CharField(max_length = 200)
	photo_url = models.URLField(max_length = 200)
	photo_title = models.CharField(max_length = 200)
	photo_date = models.DateTimeField(blank = True, null = True)
	owner = models.ForeignKey(FlickrUser)
	def __str__(self):
		return self.photo_title

# class FlickrUser(models.Model):
#     username = models.CharField(max_length = 200)
#     user_id = models.CharField(max_length = 200)
#     # votes = models.IntegerField(default = 0)
#     def __str__(self):
#     	return self.username