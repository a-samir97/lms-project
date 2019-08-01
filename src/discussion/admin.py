from django.contrib import admin
from .models import Discussion, Post, Comment
# Register your models here.
admin.site.register(Discussion)
admin.site.register(Post)
admin.site.register(Comment)
