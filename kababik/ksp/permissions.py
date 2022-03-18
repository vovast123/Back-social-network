from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):#нужно унаследовать базовый клас
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: #SAFE_METHODS безопасные типа только просмотр
            return True
        return bool(request.user and request.user.is_staff)#только для админа



class IsOwnerOrReadOnly(permissions.BasePermission):#в целом понятно но только владелец может изменять свой
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user