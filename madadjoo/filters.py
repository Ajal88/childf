import django_filters

from .models import Madadjoo, Need


class MadadjooFilter(django_filters.FilterSet):
    class Meta:
        model = Madadjoo
        fields = ['sex', 'healthStatus', 'state', 'grade']


class NeedFilter(django_filters.FilterSet):
    madadjoo__karbar__user__username = django_filters.CharFilter()
    # field_name='madadjoo', lookup_expr='username'

    class Meta:
        model = Need
        fields = ['madadjoo', 'name', 'type', 'resolved']
