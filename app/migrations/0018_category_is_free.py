# Generated by Django 3.2.4 on 2021-07-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210629_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_free',
            field=models.BooleanField(default=False, verbose_name='Бесплатный'),
        ),
    ]
