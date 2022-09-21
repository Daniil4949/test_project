from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=1000, db_index=True, verbose_name='URL', null=True, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    info = models.TextField(null=True)
    slug = models.SlugField(max_length=1000, db_index=True, verbose_name='URL', null=True, blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )
    img_url = models.TextField(null=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse('book', kwargs={'book_slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Title: {self.book.title} | Price per book: {self.book.price}$"




# Create your models here.
