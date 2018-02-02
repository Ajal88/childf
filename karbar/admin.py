from django.contrib import admin

from .models import Karbar

from django.contrib.auth.admin import UserAdmin
UserAdmin.add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name')}
        ),
    )

admin.site.register(Karbar)