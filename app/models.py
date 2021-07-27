
from django.db import models

from account.models import MyUser


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Категории'

    image = models.ImageField(upload_to='category', blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name='Слово', null='', blank='')
    is_free = models.BooleanField(default=False, verbose_name='Бесплатный')

    def __str__(self):
        return self.title


class Description(models.Model):

    class Meta:
        verbose_name_plural = 'Слово и описание'

    image = models.ImageField(upload_to='description', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='mp3', blank=True, null=True)

    def __str__(self):
        return self.title


class Favorite(models.Model):

    class Meta:
        verbose_name_plural = 'Избранные'

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='favorites')
    description = models.ForeignKey(Description, on_delete=models.CASCADE, related_name='favorites')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.user.__str__()

