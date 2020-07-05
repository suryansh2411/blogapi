from django.contrib import admin
from . models import Post, Author
from django.contrib.auth import get_user_model

admin.site.register(Post)
admin.site.register(Author)

# Register your models here.
