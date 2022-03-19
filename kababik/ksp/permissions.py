from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):#нужно унаследовать базовый клас
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: #SAFE_METHODS безопасные типа только просмотр
            return bool(request.user and request.user.is_authenticated)
        return bool(request.user and request.user.is_staff)#только для админа



class IsOwnerOrReadOnly(permissions.BasePermission):#в целом понятно но только владелец может изменять свой
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return obj.user == request.user


class IsOwnerOrReadOnlyIfAuthenticated(permissions.BasePermission):#в целом понятно но только владелец может изменять свой
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return obj.owner == request.user



class IsOwnerOrNo(permissions.BasePermission):#в целом понятно но только владелец может изменять свой
    def has_object_permission(self, request, view, obj):
        return obj.own == request.user



class IsOwnerOrReadOnlyComment(permissions.BasePermission):#в целом понятно но только владелец может изменять свой
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return obj.user == request.user


class IsOwnerOrNothingForMessage(permissions.BasePermission):#в целом понятно но только владелец может изменять свой
    def has_object_permission(self, request, view, obj):
        return obj.receiver == request.user or obj.sender == request.user