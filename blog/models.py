from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from .constant import *
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='blog/profile_pics/', blank=True)
    
    
class Blog(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/media/uploads/' ,blank= True,null= True)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    is_fav = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title 
    
# class Favorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    

    
class Rating(models.Model):
    blog = models.ForeignKey(Blog, related_name='user_rating',on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 100)
    
    def __str__(self):
        return self.blog.title