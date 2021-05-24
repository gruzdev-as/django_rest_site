from .models import Post, Tag
from .serializers import PostDetailSerializer, PostListSerializer, TagDetailSerializer, TagListSerializer
from django.shortcuts import render
from rest_framework import generics



class PostCreateView(generics.CreateAPIView):
    '''Create a post''' 

    serializer_class = PostDetailSerializer

class TagCreateView(generics.CreateAPIView):
    '''Create a tag''' 

    serializer_class = TagDetailSerializer 

class PostListView(generics.ListAPIView):
    ''' Information about all posts''' 

    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class TagListView(generics.ListAPIView):
    '''Information about all tags'''

    serializer_class = TagListSerializer
    queryset = Tag.objects.all()

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''RetrieveUpdateDestroy'''
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''RetrieveUpdateDestroy'''
    serializer_class = TagDetailSerializer
    queryset = Tag.objects.all()