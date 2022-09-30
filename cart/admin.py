from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('validity_period', 'purchased_book', 'quantity', 'date')


admin.site.register(Payment, PaymentAdmin)
# Register your models here.
