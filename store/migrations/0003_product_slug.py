# Generated by Django 4.2.2 on 2023-07-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
    ]
