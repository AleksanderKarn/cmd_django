# Generated by Django 4.1.5 on 2023-01-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_image_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publication',
            field=models.BooleanField(default=False, verbose_name='Признак публикации'),
        ),
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='Счетчик просмотров'),
        ),
    ]