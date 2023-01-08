from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post

# Create your views here.

class PostList(ListCreateAPIView): # o'qish va yozish uchun
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView): # o'chirish va o'zgartirish
    queryset = Post.objects.all()
    serializer_class = PostSerializer