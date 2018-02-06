import django_filters

from .models import Madadjoo, Need, Payment


class MadadjooFilter(django_filters.FilterSet):
    class Meta:
        model = Madadjoo
        fields = ['sex', 'healthStatus', 'state', 'grade']


class NeedFilter(django_filters.FilterSet):
    class Meta:
        model = Need
        fields = ['name', 'type', 'resolved']


class PaymentFilter(django_filters.FilterSet):

    class Meta:
        model = Payment
        fields = ['need__madadjoo__karbar__user__username', 'need__name', 'need__type', 'need__resolved']
