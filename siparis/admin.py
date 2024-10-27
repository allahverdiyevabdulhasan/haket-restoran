# siparis/admin.py
from django.contrib import admin
from .models import Siparis

@admin.register(Siparis)
class SiparisAdmin(admin.ModelAdmin):
    list_display = ('YEMEK_ADI', 'YEMEK_FIYATI', 'ICECEK_ADI', 'ICECEK_FIYATI', 'ICECEK_ADEDI', 'MUSTERI_ADI', 'MASA_NUMARASI', 'ODEME_METODU', 'SIPARIS_TARIHI', 'toplam_tutar')
    readonly_fields = ('toplam_tutar',)

# Total Ciro üçün custom admin paneli
from django.db.models import Sum

class CiroAdmin(admin.ModelAdmin):
    def toplam_ciro(self, request):
        toplam = Siparis.objects.aggregate(Sum('YEMEK_FIYATI'))['YEMEK_FIYATI__sum']
        return toplam if toplam else 0

    def changelist_view(self, request, extra_context=None):
        toplam_ciro = self.toplam_ciro(request)
        extra_context = {'toplam_ciro': toplam_ciro}
        return super().changelist_view(request, extra_context=extra_context)
