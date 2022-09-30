from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('number_of_card', 'validity_period', 'purchased_book', 'quantity', 'date')


admin.site.register(Payment, PaymentAdmin)
# Register your models here.
