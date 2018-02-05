from django.contrib import admin

from .models import Madadjoo
from .models import Need, MadadkarSupport, Payment


class NeedAdmin(admin.ModelAdmin):
    list_display = ['give_need_madadjoo', 'name', 'type', 'cost', 'amountpayed', 'resolved']
    list_filter = ['type', 'resolved', 'madadjoo__karbar__user__username']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['give_madadjoo', 'give_need_name', 'amount', 'date']
    list_filter = ['need__madadjoo__karbar__user__username', 'date']

    admin.site.register(Madadjoo)


admin.site.register(Need, NeedAdmin)
admin.site.register(MadadkarSupport)
admin.site.register(Payment, PaymentAdmin)
