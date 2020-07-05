from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
	author = serializers.CharField(source='author.username', read_only=True)
	class Meta:

		fields = ('id', 'title', 'content', 'author', 'created_at', 'updated_at',)
		model = models.Post

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('name', 'email',)
		model = models.Author
