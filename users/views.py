from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from .models import User
from .serializers import UserSerializer

#filtros para usuarios
class UserFilter(django_filters.FilterSet):
    # permite filtrar por fechas como "registrado después de" o "registrado antes de"
    date_joined__gte = django_filters.DateTimeFilter(field_name='date_joined', lookup_expr='gte')
    date_joined__lte = django_filters.DateTimeFilter(field_name='date_joined', lookup_expr='lte')
    """
        por ejemplo, 
        GET /users/?date_joined__gte=2025-01-01T00:00:00Z 
        (usuarios que entraron el  1 de enero de 2025 o después)

        GET /users/?date_joined__lte=2025-05-01T00:00:00Z 
        (usuarios que entraron el 1 de mayo de 2025 o antes)
    """
    class Meta:
        model = User
        fields = [ #campos
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'initials',
            'has_pending_receipts_to_sign',
            'nationality',
            'address',
            'phone_number',
            'employee_number',
            'role',
            'required_password_changed_done',
            'is_superuser',
            'last_login',
            'date_joined__gte',
            'date_joined__lte',
            'created_at',
            'modified_at',
        ]

#validación
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, 
            context={'request': request}
        )
        # validacion sin error 400
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            # credenciales incorrectas
            raise AuthenticationFailed('Usuario o contraseña incorrectos.')
        
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data
        return Response({**user_data, 'token': token.key}) #devolución del token para una autenticación exitosa.



#para el get, ordenamiento de usuarios (lista)
class UserListView(generics.ListAPIView):
    queryset           = User.objects.all().order_by('id')
    serializer_class   = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # filtros y paginas
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter   # ej /users/?nationality=chilean
    #users/?has_pending_receipts_to_sign=True

#vista detallada de usuarios (para filtros por id)
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]