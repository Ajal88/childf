from django.contrib import admin

from .models import Madadjoo
from .models import Need,MadadkarSupport,Payment

admin.site.register(Madadjoo)
admin.site.register(Need)
admin.site.register(MadadkarSupport)
admin.site.register(Payment)