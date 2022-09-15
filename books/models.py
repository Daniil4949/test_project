from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=1000, db_index=True, verbose_name='URL', null=True, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=1000, db_index=True, verbose_name='URL', null=True, blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_slug': self.slug})

    def __str__(self):
        return f"{self.title}"
# Create your models here.
