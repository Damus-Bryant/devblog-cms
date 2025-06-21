from django.contrib import admin
from .models import Post
from categories.models import Category

admin.site.register(Post)
admin.site.register(Category)