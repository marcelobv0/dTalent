from django.urls import path
from .views import ReceiptListCreateView, ReceiptFileView

#urls del endpoint /receipts (por ej /receipts/?lista=[si es que genera una lista de más de una página, o filtros]; receipts/{id}/file)
urlpatterns = [
    path('',         ReceiptListCreateView.as_view(), name='receipt-list-create'),       # GET /receipts/
    path('<int:pk>/file/', ReceiptFileView.as_view(),   name='receipt-file'), # GET /receipts/{id}/file
]
