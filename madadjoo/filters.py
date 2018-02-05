import django_filters

from .models import Madadjoo, Need


class MadadjooFilter(django_filters.FilterSet):
    class Meta:
        model = Madadjoo
        fields = ['sex', 'healthStatus', 'state', 'grade']


class NeedFilter(django_filters.FilterSet):
    class Meta:
        model = Need
        fields = ['name', 'type', 'resolved']
