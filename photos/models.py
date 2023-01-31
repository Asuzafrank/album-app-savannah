from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

    

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100, null=False,blank=False)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(null =False, blank = False)
    description = models.TextField(max_length=100, null=False,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.description

 