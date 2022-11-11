import django_filters
from .models import Voo

class VooFilter(django_filters.FilterSet):
    companhiaAerea = django_filters.CharFilter(lookup_expr='icontains')
    aeroportoOrigem = django_filters.CharFilter(lookup_expr='icontains')
    companhiaDestino = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Voo
        fields = ('companhiaAerea', 'aeroportoOrigem', 'aeroportoDestino')