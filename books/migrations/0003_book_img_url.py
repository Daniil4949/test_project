# Generated by Django 4.1.1 on 2022-09-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img_url',
            field=models.TextField(null=True),
        ),
    ]
