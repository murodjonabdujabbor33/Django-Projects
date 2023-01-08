from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta: # API imizda modelimzning qaysi qismlari chiqishini belgilaymiz
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post
