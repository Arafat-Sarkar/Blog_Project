from django.contrib import admin
from .import models
# Register your models here.
admin.site.register(models.Blog)
admin.site.register(models.Rating)
# admin.site.register(models.Favorite) 
admin.site.register(models.Profile) 
