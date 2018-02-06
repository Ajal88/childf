from django.contrib import admin

from .models import Madadjoo
from .models import Need, MadadkarSupport, Payment


class MadadjooAdmin(admin.ModelAdmin):
    list_display = ['madadkar_firstname', 'madadkar_lastname', 'fatherName', 'sex', 'city', 'grade', 'state',
                    'healthStatus', 'give_madadkar']
    list_filter = ['madadkar_field', 'sex', 'state', 'city']


class NeedAdmin(admin.ModelAdmin):
    list_display = ['give_need_madadjoo', 'name', 'type', 'cost', 'amountpayed', 'resolved']
    list_filter = ['type', 'resolved', 'madadjoo__karbar__user__username']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['give_madadjoo', 'give_need_name', 'amount', 'date']
    list_filter = ['need__madadjoo__karbar__user__username', 'date']


admin.site.register(Madadjoo, MadadjooAdmin)
admin.site.register(Need, NeedAdmin)
admin.site.register(MadadkarSupport)
admin.site.register(Payment, PaymentAdmin)
