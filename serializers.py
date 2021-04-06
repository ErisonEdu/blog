from rest_framework import serializers
from .models import Post

class PostlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'author',
            'body',
            'publish',
            'created',
            'updated',
        ]