
from .views import ContactFormView, PostCreateView, PostDetailView, PostListView, TagCreateView, TagListView, TagDetailView
from django.contrib import admin
from django.urls import path, include

app_name = 'site_feed'
urlpatterns = [
    path('post/create/', PostCreateView.as_view()),
    path('post/all/', PostListView.as_view()),
    path('post/detail/<int:pk>', PostDetailView.as_view()),
    
    path('tag/create/', TagCreateView.as_view()),
    path('tag/all/', TagListView.as_view()),
    path('tag/detail/<int:pk>', TagDetailView.as_view()),

    path('feedback/', ContactFormView.as_view()),
]