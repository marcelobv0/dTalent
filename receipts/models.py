from django.db import models
from django.conf import settings

#creado del modelo de "recibos"
class Receipt(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='receipts'
    ) #definición de las propiedades de los recibos
    created_at   = models.DateTimeField(auto_now_add=True)
    modified_at  = models.DateTimeField(auto_now=True)
    is_active    = models.BooleanField(default=True)
    full_date    = models.DateTimeField()
    year         = models.PositiveIntegerField()
    month        = models.PositiveSmallIntegerField()
    type         = models.CharField(max_length=50)
    is_sended    = models.BooleanField(default=False)
    is_readed    = models.BooleanField(default=False)
    is_signed    = models.BooleanField(default=False)
    sended_date  = models.DateTimeField(null=True, blank=True)
    readed_date  = models.DateTimeField(null=True, blank=True)
    signed_date  = models.DateTimeField(null=True, blank=True)
    file = models.FileField(upload_to='receipts/', null=True, blank=True)  # ← this line

    # devuelve el numero del recibo para el usuario asociado al recibo
    def __str__(self):
        return f"Receipt #{self.pk} for {self.employee.username}"
