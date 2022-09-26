# Generated by Django 4.0.6 on 2022-09-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_remove_author_first_name_remove_author_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True, unique=True, verbose_name='URL'),
        ),
    ]