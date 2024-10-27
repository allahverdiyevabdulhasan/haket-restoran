from django.urls import path
from .views import SiparisEkle, SiparisGoster, ExportPDF

urlpatterns = [
    path('', SiparisEkle.as_view(), name='siparis_ekle'),  # Ana sayfa sipariş ekleme formunu gösterecek
    path('siparisler/', SiparisGoster.as_view(), name='siparis_goster'),  # Siparişleri görüntüleme
    path('export_pdf/', ExportPDF.as_view(), name='export_pdf'),  # PDF dışa aktarma
]
