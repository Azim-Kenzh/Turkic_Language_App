# Generated by Django 3.2.4 on 2021-07-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_myuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='payment_end',
            field=models.DateField(null=True),
        ),
    ]