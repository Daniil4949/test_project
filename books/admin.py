from django.contrib import admin
from .models import Book, Category, Cart, Author


class CategoryAdmin(admin.ModelAdmin):
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


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Author, AuthorAdmin)


# Register your models here.
