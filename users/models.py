from django.contrib.auth.models import AbstractUser
from django.db import models

#generación del modelo de los usuarios (propiedades)
class User(AbstractUser):
    initials = models.CharField(max_length=10, blank=True)
    has_pending_receipts_to_sign = models.BooleanField(default=False)
    nationality = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    employee_number = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=50, blank=True)
    required_password_changed_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    #self que devuelve nombre del usuario
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
