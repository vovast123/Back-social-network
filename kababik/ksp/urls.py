from django.urls import path,include,re_path
from . import views
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()#DefaultRouter - помагает понять по какой ссылке апи перейдя только на api/v1/ а так же можна смотреть по name - women-list wimen-detail и тд (зависит от модели)
router.register(r'customuser',CustomUserAPI)

routerpost = routers.DefaultRouter()
routerpost.register(r'post',PostAPI)

routercomment = routers.DefaultRouter()
routercomment.register(r'comment',CommentApi)

routerImage = routers.DefaultRouter()
routerImage.register(r'image',ImageApi)

routerMasege = routers.DefaultRouter()
routerMasege.register(r'masege',MessageApi)


routerFolow = routers.DefaultRouter()
routerFolow.register(r'folow',FolowerAPI)

urlpatterns = [
    path('api/v1/auth/',include('rest_framework.urls')),
    path('api/v1/customuser/',views.CustomUserAPI.as_view()),
    path('api/v1/customuser/<int:pk>/',views.CustomUserAPI.as_view()),
    path('api/v1/',include(routerMasege.urls)),
    path('api/v1/',include(routerFolow.urls)),
    path('api/v1/',include(routerImage.urls)),
    path('api/v1/',include(routerpost.urls)),
    path('api/v1/',include(routercomment.urls)),
    path('auth/',include('djoser.urls.authtoken')),
    path('auth/',include('djoser.urls')),
    
]
