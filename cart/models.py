from django.db import models
from books.models import Cart, Book
from users.models import CustomUser


class Payment(models.Model):
    """Object 'Payment' has all the attributes of the payment except for the cvv code.
     It is possible to save it as a password. But  I have decided to do not save it at all """
    number_of_card = models.CharField(max_length=16)
    validity_period = models.CharField(max_length=5, default='00/00')
    purchased_book = models.ForeignKey(Book, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
