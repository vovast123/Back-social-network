from django.urls import path,include,re_path
from . import views
from .views import *
from rest_framework import routers

urlpatterns = [
    path('api/v1/auth/',include('rest_framework.urls')),
    path('api/v1/customuser/',views.CustomUserAPI.as_view()),
    path('api/v1/customuser/<int:pk>/',views.CustomUserAPI.as_view()),
    path('api/v1/post/',views.PostAPIView.as_view()),
    path('api/v1/post/<int:pk>/',views.PostAPIUpdate.as_view()),
    path('api/v1/folow/',views.FolowAPIView.as_view()),
    path('api/v1/folow/<int:pk>/',views.FolowAPIAll.as_view()),
    path('api/v1/image/',views.ImageApi.as_view()),
    path('api/v1/image/<int:pk>/',views.ImageAPIAll.as_view()),
    path('api/v1/comment/',views.CommentAPI.as_view()),
    path('api/v1/comment/<int:pk>/',views.CommentAPIAll.as_view()),
    path('api/v1/message/',views.MessageApi.as_view()),
    path('api/v1/message/<int:pk>/',views.MessageApiDetail.as_view()),
    path('api/v1/receiver/',views.ReceiverApi.as_view()),
    path('api/v1/receiver/<int:pk>/',views.MessageApiDetail.as_view()),

    path('auth/',include('djoser.urls.authtoken')),
    path('auth/',include('djoser.urls')),
    
]
