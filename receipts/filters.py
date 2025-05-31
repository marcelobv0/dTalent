import django_filters
from .models import Receipt

class ReceiptFilter(django_filters.FilterSet):
    
    # ayuda a los filtros, con parámetros como "contiene x" o "desde la fecha hacia delante (o hacia atrás)"
    full_date__gte = django_filters.DateTimeFilter(field_name='full_date', lookup_expr='gte')
    type__icontains = django_filters.CharFilter(field_name='type', lookup_expr='icontains')
    full_date__lte = django_filters.DateTimeFilter(field_name='full_date', lookup_expr='lte')

    class Meta:
        model  = Receipt
        fields = [  #filtros correspondientes a los recibos. (propiedades)
            'id',
            'employee',
            'created_at',
            'modified_at',
            'is_active',
            'full_date',
            'year',
            'month',
            'type',
            'is_sended',
            'is_readed',
            'is_signed',
            'sended_date',
            'readed_date',
            'signed_date',
        ]
