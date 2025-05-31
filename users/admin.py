from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

#para el registro de usuarios desde el endpoint admin
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    # campos que se mostrarán en la lista de usuarios (/admin/users/)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'is_superuser',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'role',
        'is_superuser',
        'is_staff',
        'is_active',
    )

    # sólo lectura ya que no pueden ser modificados
    readonly_fields = (
        'last_login',
        'date_joined',
        'created_at',
        'modified_at',
    )

    # controla qué campos aparecen en la página de “editar usuario”
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
            )
        }),
        ('Información personal', {
            'fields': (
                'first_name',
                'last_name',
                'initials',
                'email',
                'nationality',
                'address',
                'phone_number',
                'employee_number',
                'role',
            )
        }),
        ('Permisos', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Estado de recibos', {
            'fields': (
                'has_pending_receipts_to_sign',
                'required_password_changed_done',
            )
        }),
        ('Fechas importantes (solo lectura)', {
            'fields': (
                'last_login',
                'date_joined',
                'created_at',
                'modified_at',
            )
        }),
    )

    # campos que aparecen al pulsar “Add user” inicialmente
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'first_name',
                'last_name',
                'initials',
                'nationality',
                'address',
                'phone_number',
                'employee_number',
                'role',
                'password1',
                'password2',
            ),
        }),
    )

    search_fields = ('username', 'email', 'first_name', 'last_name') #campos de búsqueda
    ordering = ('username',) #ordenamiento
