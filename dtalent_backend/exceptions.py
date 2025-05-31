from rest_framework.views import exception_handler as drf_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import (
    AuthenticationFailed, NotAuthenticated,
    PermissionDenied, NotFound, ValidationError
)

def custom_exception_handler(exc, context):
    # respuesta de error por defecto
    response = drf_handler(exc, context)

    # si DRF no puede manejar la excepción, error=500
    if response is None:
        return Response(
            {"error": {
                "code": "server_error",
                "message": "Error interno del servidor."
            }},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    # mapear excepciones para casos específicos del API
    if isinstance(exc, NotAuthenticated):
        code, msg = "not_authenticated", "No se proporcionaron credenciales."
    elif isinstance(exc, AuthenticationFailed):
        code, msg = "authentication_failed", str(exc.detail)
    elif isinstance(exc, PermissionDenied):
        code, msg = "permission_denied", "No tienes permiso para ver usuarios."
    elif isinstance(exc, NotFound):
        code, msg = "not_found", "Usuario no encontrado."
    elif isinstance(exc, ValidationError):
        code, msg = "invalid_input", "Datos proporcionados inválidos."
    else:
        # si no, volver al detalle del error de DRF
        code, msg = getattr(exc, 'default_code', 'error'), response.data

    return Response(
        {"error": {
            "code": code,
            "message": msg,
            # incluir detalles de nivel sobre el error.
            **({"details": response.data} if isinstance(exc, ValidationError) else {})
        }},
        status=response.status_code
    )
