from django.shortcuts import render
from rest_framework import generics, viewsets

from .permissions import IsAdminOrReadOnly, IsOwnerOrNo, IsOwnerOrNothingForMessage, IsOwnerOrReadOnly, IsOwnerOrReadOnlyComment, IsOwnerOrReadOnlyIfAuthenticated
from .serializers import CommentSerializer, FolowerSerializer, ImageSerializer, MessageSerializer, PostSerializer, UserCustomSerializer
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response 
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

class CustomAPIListPagination(PageNumberPagination):#отдельная погинация под клас
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000 


class CustomUserAPI(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCustomSerializer
    pagination_class = CustomAPIListPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):#фильтровать но и возможность по id переходить
        pk = self.kwargs.get("pk")
        if not pk:           
            return CustomUser.objects.all()
        return CustomUser.objects.filter(pk=pk)


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomAPIListPagination


class PostAPIUpdate(generics.RetrieveUpdateDestroyAPIView):#изминяет
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnlyIfAuthenticated,)

class FolowAPIView(generics.ListCreateAPIView):
    queryset = Folower.objects.all()
    serializer_class = FolowerSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomAPIListPagination

class FolowAPIAll(generics.RetrieveUpdateDestroyAPIView):#изминяет
    queryset = Folower.objects.all()
    serializer_class = FolowerSerializer
    permission_classes = (IsAuthenticated,)

class ImageApi(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomAPIListPagination
    def get_queryset(self):#фильтровать но и возможность по id переходить
        user = self.request.user
        return Image.objects.filter(own=user)

class ImageAPIAll(generics.RetrieveUpdateDestroyAPIView):#изминяет
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsOwnerOrNo,)


class CommentAPI(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomAPIListPagination

class CommentAPIAll(generics.RetrieveUpdateDestroyAPIView):#изминяет
    queryset = Reviews.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnlyComment,)


class MessageApi(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomAPIListPagination
    def get_queryset(self):#фильтровать но и возможность по id переходить
        user = self.request.user
        return Message.objects.filter(sender = user)

class MessageApiDetail(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerOrNothingForMessage,)


class ReceiverApi(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomAPIListPagination
    def get_queryset(self):#фильтровать но и возможность по id переходить
        user = self.request.user
        return Message.objects.filter(receiver = user)

