'''Serializers''' 


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
   

    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):


    class Meta: 
        model = Post
        fields = '__all__'


