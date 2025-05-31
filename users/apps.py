from django.apps import AppConfig

#para la configuración de la app (users)
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
