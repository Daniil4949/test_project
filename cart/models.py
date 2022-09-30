from django.db import models
from books.models import Cart, Book


class Payment(models.Model):
    number_of_card = models.CharField(max_length=16)
    validity_period = models.CharField(max_length=5, default='00/00')
    purchased_book = models.ForeignKey(Book, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
