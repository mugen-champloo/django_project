# Generated by Django 4.2.2 on 2023-07-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='info',
            field=models.TextField(blank=True, verbose_name='Текст статьи'),
        ),
    ]
