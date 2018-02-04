from django.contrib import admin

from .models import Hamyar


class HamyarAdmin(admin.ModelAdmin):
    list_display = ['id', 'hamyar_username', 'phoneNumber']
    list_filter = ['karbar__user__username']
    search_fields = ['karbar__user__username', 'id']


admin.site.register(Hamyar, HamyarAdmin)
