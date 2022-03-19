import email
from email.policy import default
from pydoc import describe
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    image = models.ImageField('Фото',upload_to='users/',default='nophoto.png')
    describe = models.CharField('Биография',max_length=255,blank=True)



class Post(models.Model):
    image = models.ManyToManyField('Image',verbose_name="Фотки",related_name='image_to_post')
    likes = models.ManyToManyField(CustomUser, blank=True, related_name='likes')
    text = models.CharField('Описание',max_length=255)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='own_post')
    time = models.DateTimeField(auto_now_add=True,verbose_name="дата публикации")
    

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'



class Reviews(models.Model):
    """Отзывы"""
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    post = models.ForeignKey(Post,related_name="comment", verbose_name="Пост", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,related_name="commentparent", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.post}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"



class Image(models.Model):
    own = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="own_image")
    image = models.ImageField('Фото',upload_to='post/')
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотки"



class Folower(models.Model):
    owner = models.ForeignKey(CustomUser, related_name="owner_to", on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(CustomUser, related_name="user_to", on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'{self.owner} - {self.user}'
    
    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"



class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)