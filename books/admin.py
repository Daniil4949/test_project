from django.contrib import admin
from .models import Book, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ('name',)}


class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
