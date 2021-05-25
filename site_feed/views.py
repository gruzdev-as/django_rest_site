
from .models import Post, Tag

from .serializers import *

from django.core.mail import send_mail

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


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

class ContactFormView(APIView):
    '''Feedback form view''' 
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        ''' POST ''' 
        serializer_class = ContactSerializer(data = request.data)
        if serializer_class.is_valid():
            data = serializer_class.validated_data
            from_email = data.get('email')
            title = data.get('title')
            message = data.get('message')
            send_mail(title, message, from_email, ['Send to email'],)

            return Response({'success' : 'Sent'})
        