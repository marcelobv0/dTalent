from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


#archivo forms para la creación y hashing correcta de usuarios mediante el endpoint /admin
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        # lista de los campos que deben mostrarse en la pantalla de 'crear usuario' 
        fields = (
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
        )


#form para el cambio a usuarios existentes en el endpoint /admin mediante campos de Django
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        # campos a editar:
        fields = (
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
            'has_pending_receipts_to_sign',
            'required_password_changed_done',
            'is_superuser',
            'is_staff',
            'is_active',
        )
