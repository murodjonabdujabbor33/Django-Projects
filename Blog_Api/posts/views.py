from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from .models import Post

# Create your views here.

class PostList(ListCreateAPIView): # o'qish va yozish uchun
    # permission_classes = (permissions.IsAuthenticated,) # saytga logini orqali kirganlarga barcha o'zgartirishlarga ruxsat beriladi.
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView): # o'chirish va o'zgartirish
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer