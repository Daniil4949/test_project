from django.contrib import admin
from .models import Book, Category, Cart, Author, Rating


class CategoryAdmin(admin.ModelAdmin):
    """prepopulated field automatically create slug from the name of the category"""
    list_display = ('name',)
    prepopulated_fields = {"slug": ('name',)}


class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ('title',)}


class CartAdmin(admin.ModelAdmin):
    list_display = ('book', 'user')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'img_url', 'info')
    prepopulated_fields = {"slug": ('name',)}


class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'score')


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Rating, RatingAdmin)

# Register your models here.
