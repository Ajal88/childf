import django_filters

from .models import Madadjoo


class MadadjooFilter(django_filters.FilterSet):
    class Meta:
        model = Madadjoo
        fields = ['sex', 'healthStatus', 'state', 'grade']
