from django.db import models
from books.models import Cart


class Payment(models.Model):
    number_of_cart = models.CharField(max_length=16)
    validity_period_month = models.CharField(max_length=2)
    validity_period_year = models.CharField(max_length=2)
    purchased_book = models.ForeignKey(Cart, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)
# Create your models here.
