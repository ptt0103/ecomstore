from django.contrib import admin

# Register your models here.
from payment.models import payment_status
admin.site.register(payment_status)
