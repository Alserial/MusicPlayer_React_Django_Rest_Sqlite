from django.db import models

# Create your models here.
    
class Musics(models.Model):
    musicID = models.AutoField(primary_key=True)
    musicName = models.CharField(max_length=100)
    musicUrl = models.CharField(max_length=100, null=True, blank=True)
    musicType = models.CharField(max_length=100, null=True, blank=True)

class MusicList(models.Model):
    musicListId = models.AutoField(primary_key=True)
    musicListName = models.CharField(max_length=100, default='favourite')
    musicListProfilePic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    userBelongTo = models.CharField(max_length=100)
    musicIn = models.ManyToManyField(Musics)
    
class UserRole(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    role = models.CharField(max_length=100, default="user")
    firstname = models.CharField(max_length=100, default="user")
    lastname = models.CharField(max_length=100, default="user")
    musicListIn = models.ManyToManyField(MusicList)
    
    