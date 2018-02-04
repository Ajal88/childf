from django.contrib import admin

from .models import Madadkar


class MadadkarAdmin(admin.ModelAdmin):
    list_display = ['id', 'madadkar_username', 'NationalCode', 'education', 'city', 'phoneNumber', 'dateOfEmployeement']
    list_filter = ['city', 'education', 'salary']
    search_fields = ['karbar__user__username', 'id', 'NationalCode', 'city', 'salary']


admin.site.register(Madadkar, MadadkarAdmin)
