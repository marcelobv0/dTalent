from django.contrib import admin
from .models import Receipt

#registrar recibos desde el endpoint 'admin'
@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ( #propiedades agregables a los recibos desde el endpoint admin
        'id',
        'employee',
        'year',
        'month',
        'type',
        'is_signed',
        'is_readed',
        'is_sended',
        'created_at',
    )
    list_filter = ( #filtros posibles para recibos
        'year',
        'month',
        'type',
        'is_signed',
        'is_readed',
        'is_sended',
    )
    search_fields = ('employee__username', 'type') #espacios posibles de búsqueda para recibos
