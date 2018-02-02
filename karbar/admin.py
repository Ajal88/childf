from django.contrib import admin

from karbar.models import *

from django.contrib.auth.admin import UserAdmin

UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'password1', 'password2', 'first_name', 'last_name')}
     ),
)

admin.site.register(Karbar)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Request)
