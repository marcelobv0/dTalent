from rest_framework import serializers
from .models import Receipt

#serializadores para cada propiedad
class ReceiptSerializer(serializers.ModelSerializer):
    createdAt        = serializers.DateTimeField(source='created_at')
    modifiedAt       = serializers.DateTimeField(source='modified_at')
    isActive         = serializers.BooleanField(source='is_active')
    fullDate         = serializers.DateTimeField(source='full_date')
    isSended         = serializers.BooleanField(source='is_sended')
    isReaded         = serializers.BooleanField(source='is_readed')
    isSigned         = serializers.BooleanField(source='is_signed')
    sendedDate       = serializers.DateTimeField(source='sended_date', allow_null=True)
    readedDate       = serializers.DateTimeField(source='readed_date', allow_null=True)
    signedDate       = serializers.DateTimeField(source='signed_date', allow_null=True)
    employeeFullName = serializers.CharField(source='employee.full_name', read_only=True)
    employeeNumber   = serializers.IntegerField(source='employee.employee_number', read_only=True)

    class Meta:
        model = Receipt
        fields = [ #propiedades de recibos
            'id', 'createdAt', 'modifiedAt', 'isActive',
            'fullDate', 'year', 'month', 'type',
            'isSended', 'isReaded', 'isSigned',
            'sendedDate', 'readedDate', 'signedDate',
            'employee', 'employeeFullName', 'employeeNumber',
        ]
