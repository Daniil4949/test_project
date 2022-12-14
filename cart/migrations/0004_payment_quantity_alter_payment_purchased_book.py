# Generated by Django 4.0.6 on 2022-09-30 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_book_writer'),
        ('cart', '0003_remove_payment_validity_period_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payment',
            name='purchased_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book'),
        ),
    ]
