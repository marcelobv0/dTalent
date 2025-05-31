from rest_framework import generics, permissions
from .models import Receipt
from .serializers import ReceiptSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse, Http404
from .filters import ReceiptFilter

class ReceiptListCreateView(generics.ListCreateAPIView):
    """
    GET  /receipts/            -> lista recibos con filtros y páginación
    POST /receipts/            -> crea recibos (opcional: alzar archivos)
    """
    queryset           = Receipt.objects.all().order_by('id')
    serializer_class   = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes     = [MultiPartParser, FormParser]

    filter_backends    = [DjangoFilterBackend]
    filterset_class    = ReceiptFilter

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)

# devuelve el archivo pdf del archivo
class ReceiptFileView(generics.RetrieveAPIView):
    """
    GET /receipts/{id}/file/
      - retorna el recibo adjunto en pdf
      - o un error 404 si no existe un archivo adjunto
    
    """
    serializer_class   = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset           = Receipt.objects.all()

    def get(self, request, *args, **kwargs):
        # retorna el recibo (o da error 404)
        receipt = self.get_object()
        # si no hay archivo, entonces ->
        if not receipt.file:
            raise Http404("No file attached to this receipt.")
        # si hay archivo, abrir y ejecutarlo como pdf
        file_handle = receipt.file.open('rb')
        return FileResponse(file_handle, content_type='application/pdf')


