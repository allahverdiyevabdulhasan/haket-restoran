from django.db import models

class Siparis(models.Model):
    YEMEK_ADI = models.CharField(max_length=100)  # Yemək adı
    YEMEK_FIYATI = models.DecimalField(max_digits=10, decimal_places=2, null=False)  # Yemək qiyməti
    ICECEK_ADI = models.CharField(max_length=100, blank=True)  # İçki adı (opsiyonel)
    ICECEK_FIYATI = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # İçki qiyməti (varsayılan 0)
    ICECEK_ADEDI = models.PositiveIntegerField(default=0)  # İçki adedi (varsayılan 0)
    MUSTERI_ADI = models.CharField(max_length=100)  # Müştəri adı
    MASA_NUMARASI = models.PositiveIntegerField()  # Masa nömrəsi
    ODEME_METODU = models.CharField(max_length=10, choices=[('naqd', 'Nağd'), ('kart', 'Kartla')], default='naqd')  # Ödəniş metodu (varsayılan Nağd)
    SIPARIS_TARIHI = models.DateTimeField(auto_now_add=True)  # Sipariş tarixi

    @property
    def toplam_tutar(self):
        # Toplam tutarı hesablamaq
        yemek_fiyati = self.YEMEK_FIYATI or 0
        icecek_fiyati = self.ICECEK_FIYATI or 0
        icecek_adedi = self.ICECEK_ADEDI or 0
        return yemek_fiyati + (icecek_fiyati * icecek_adedi)

    def __str__(self):
        # Modelin string representation-u
        return f"{self.YEMEK_ADI} - {self.MUSTERI_ADI} ({self.MASA_NUMARASI})"
