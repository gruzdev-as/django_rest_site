'''Serializers''' 

from django.core.mail import message
from .models import Post, Tag
from rest_framework import serializers

class TagDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)

class TagListSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Tag
        fields = ('name',)

class PostDetailSerializer(serializers.ModelSerializer):
   
    tag = TagDetailSerializer(many = True)

    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):

    tag = TagDetailSerializer(many = True)

    class Meta: 
        model = Post
        fields = '__all__'

class ContactSerializer(serializers.Serializer):
    ''' Serializer for feedback form ''' 
    name = serializers.CharField()
    title = serializers.CharField()
    email = serializers.EmailField()
    message = serializers.CharField()