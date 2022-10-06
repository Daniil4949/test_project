from django.db import models
from django.urls import reverse
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=1000, db_index=True, verbose_name='URL', null=True, blank=True, unique=True)

    def get_absolute_url(self):
        """You can use 'category.get_absolute_url' in html-templates"""
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    """There are two foreign keys in the models: writer(the author) and the category.
    the field 'foreign key' - one to mane rel. """
    title = models.CharField(max_length=50)
    info = models.TextField(null=True)
    slug = models.SlugField(max_length=1000, db_index=True, verbose_name='URL', null=True, blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )
    img_url = models.TextField(null=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    writer = models.ForeignKey('Author', null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """You can use 'book.get_absolute_url' in html-templates"""
        return reverse('book', kwargs={'book_slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class Cart(models.Model):
    """The object 'Cart' has the user field and the selected book. It is additional
    model for the cart. Actually it is just many to many rel because one book can be in many carts of users and
    one user can add to the cart different books"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        """Method '__str__' if for the users and for the representation of the Book object"""
        return f"Title: {self.book.title} | Price per book: {self.book.price}$"


class Author(models.Model):
    name = models.CharField(max_length=40, default='Author')
    slug = models.SlugField(max_length=1000, db_index=True, verbose_name='URL', null=True, blank=True, unique=True)
    img_url = models.TextField(null=True)
    info = models.TextField()

    def __str__(self):
        """This method return the name of the author"""
        return f'{self.name}'


class Rating(models.Model):
    """Object 'Rating' has own validation. The default score is equal to zero and
    is the defined minimum. The max value of the score filed is equal to 5"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0), ])

    def __str__(self):
        return f"{self.user}'s rating on {self.book}"


class Comment(models.Model):
    """ The object 'Comment' has two foreign keys - book and the user.
    There also time of the creating comment, it is defined by default value"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return f'This is a comment of {self.user.username} on the {self.book.title}'
# Create your models here.
