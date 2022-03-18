from rest_framework import serializers
from .models import *


class UserCustomSerializer(serializers.ModelSerializer):
    owner_to = serializers.StringRelatedField(many=True)
    user_to = serializers.StringRelatedField(many=True)


    class Meta:
        model = CustomUser
        fields = ("id","username","email","image","describe",'user_to','owner_to')# если хотим все поля


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())#запрещает брать другово юзера
    comment = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = "__all__"# если хотим все поля




class ImageSerializer(serializers.ModelSerializer):
    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault)#запрещает брать другово юзера
    class Meta:
        model = Image
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault)#запрещает брать другово юзера
    class Meta:
        model = Reviews
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=CustomUser.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=CustomUser.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']


class FolowerSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Folower
        fields = ['owner', 'user', 'id']

        