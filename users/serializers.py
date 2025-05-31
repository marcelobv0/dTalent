from rest_framework import serializers
from .models import User

#serializador del usuario
class UserSerializer(serializers.ModelSerializer):
    initials = serializers.CharField()
    hasPendingReceiptsToSign = serializers.BooleanField(source='has_pending_receipts_to_sign')
    lastLogin = serializers.DateTimeField(source='last_login')
    isSuperuser = serializers.BooleanField(source='is_superuser')
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    fullName = serializers.CharField(source='full_name', read_only=True)
    dateJoined = serializers.DateTimeField(source='date_joined')
    createdAt = serializers.DateTimeField(source='created_at')
    modifiedAt = serializers.DateTimeField(source='modified_at')
    phoneNumber = serializers.CharField(source='phone_number')
    employeeNumber = serializers.IntegerField(source='employee_number')
    requiredPasswordChangedDone = serializers.BooleanField(source='required_password_changed_done')

    class Meta:
        model = User
        fields = [ #propiedades
            'id', 'initials', 'hasPendingReceiptsToSign', 'lastLogin',
            'isSuperuser', 'username', 'firstName', 'lastName',
            'nationality', 'email', 'fullName', 'role',
            'dateJoined', 'createdAt', 'modifiedAt',
            'address', 'phoneNumber', 'employeeNumber',
            'requiredPasswordChangedDone',
        ]
