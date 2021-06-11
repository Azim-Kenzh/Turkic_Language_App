
from django.db import models

from account.models import MyUser


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Категории'

    image = models.ImageField(upload_to='category', blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name='Слово', null='', blank='')
    # slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Word(models.Model):

    class Meta:
        verbose_name_plural = 'Слово'

    title = models.CharField(max_length=200, verbose_name='Слово', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

class Description(models.Model):

    class Meta:
        verbose_name_plural = 'Описание-слов'

    image = models.ImageField(upload_to='description', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Слово')
    audio_file = models.FileField(upload_to='mp3')

    def __str__(self):
        return self.title


class Favorite(models.Model):

    class Meta:
        verbose_name_plural = 'Избранные'

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='favorites')
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='favorites')
    favorite = models.BooleanField(default=False, verbose_name='Избранный')


    def __str__(self):
        return self.user.__str__()