from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from karbar.models import *


class KarbarAdmin(admin.ModelAdmin):
    # fields = ['id', 'user__username', 'phone_number']
    list_display = ['id', 'user_type']


UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')}
     ),
)

admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Request)
admin.site.register(Karbar, KarbarAdmin)
