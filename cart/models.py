from django.db import models
from books.models import Cart


class Payment(models.Model):
    number_of_cart = models.CharField(max_length=16)
    validity_period = models.CharField(max_length=5, default='00/00')
    purchased_book = models.ForeignKey(Cart, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)
