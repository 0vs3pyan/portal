# Generated by Django 3.2.4 on 2021-07-25 08:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20210725_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 25, 8, 24, 54, 16165, tzinfo=utc), verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 25, 8, 24, 54, 16186, tzinfo=utc), verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 25, 8, 24, 54, 15622, tzinfo=utc), verbose_name='дата создания'),
        ),
    ]
