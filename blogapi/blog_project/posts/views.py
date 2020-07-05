from rest_framework import generics
from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer


class PostList(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class AuthorDetail(generics.ListAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
