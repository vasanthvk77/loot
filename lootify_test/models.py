# from djongo import models  

# class Song(models.Model):
#     title = models.CharField(max_length=255)
#     artist = models.CharField(max_length=255)
    
#     image = models.ImageField(upload_to='images/')
#     audio = models.FileField(upload_to='songs/')
from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio/')


    

    def __str__(self):
        return self.title
