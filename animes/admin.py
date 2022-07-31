from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Anime)
admin.site.register(models.Tag)
admin.site.register(models.Review)
admin.site.register(models.Image)