
from django.db import models

from account.models import MyUser


class Category(models.Model):

    class Meta:
        verbose_name = 'Kategoriler'

    image = models.ImageField(upload_to='category', blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name='Isim', null='', blank='')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Word(models.Model):

    class Meta:
        verbose_name = 'Kelimeler'

    title = models.CharField(max_length=200, verbose_name='Isim', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='kategori')

    def __str__(self):
        return self.title

class Description(models.Model):

    class Meta:
        verbose_name = 'Açıklama-Kelimesi'

    image = models.ImageField(upload_to='description', blank=True, null=True)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Isim')
    audio_file = models.FileField(upload_to='mp3')


class Favorite(models.Model):

    class Meta:
        verbose_name = 'Favoriler'

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='favorites')
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='favorites')
    favorite = models.BooleanField(default=False, verbose_name='Favoriler')


    def __str__(self):
        return self.user.__str__()