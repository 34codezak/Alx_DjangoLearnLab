from rest_framework import serializers
from .models import CustomUser, Post, Comment
from rest_framework.authtoken.models import Token

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content", "author", "created_at", "updated_at"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "author", "post", "created_at", "updated_at"]     