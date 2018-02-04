from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from karbar.models import *


class KarbarAdmin(admin.ModelAdmin):
    list_display = ['id', 'karbar_username', 'user_type']
    list_filter = ['user_type']
    search_fields = ['user_type', 'user__username', 'id']



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
