from django.contrib import admin

from .models import Hamyar


class HamyarAdmin(admin.ModelAdmin):
    # fields = ['id', 'user__username', 'phone_number']
    list_display = ['id', 'phoneNumber', 'karbar']


admin.site.register(Hamyar, HamyarAdmin)
