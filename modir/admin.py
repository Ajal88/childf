from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Modir

admin.site.register(Modir)

admin.site.register(LogEntry)
