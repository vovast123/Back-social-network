from urllib import request
from django.shortcuts import render
from rest_framework import generics, viewsets

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import CommentSerializer, FolowerSerializer, ImageSerializer, MessageSerializer, PostSerializer, UserCustomSerializer
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response 
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

class CustomUserAPIListPagination(PageNumberPagination):#отдельная погинация под клас
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000 


class CustomUserAPI(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCustomSerializer
    pagination_class = CustomUserAPIListPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):#фильтровать но и возможность по id переходить
        pk = self.kwargs.get("pk")
        if not pk:           
            return CustomUser.objects.all()
        return CustomUser.objects.filter(pk=pk)




class PostAPI(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class FolowerAPI(viewsets.ModelViewSet):
    queryset = Folower.objects.all()
    serializer_class = FolowerSerializer
    permission_classes = (AllowAny,)

class ImageApi(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsOwnerOrReadOnly,)
class CommentApi(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MessageApi(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer