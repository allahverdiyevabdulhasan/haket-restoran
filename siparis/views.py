from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Siparis
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse

class SiparisGoster(ListView):
    model = Siparis
    template_name = 'siparis/siparis_goster.html'
    context_object_name = 'siparisler'

class SiparisEkle(CreateView):
    model = Siparis
    template_name = 'siparis/siparis_ekle.html'
    fields = ['YEMEK_ADI', 'YEMEK_FIYATI', 'ICECEK_ADI', 'ICECEK_FIYATI', 'ICECEK_ADEDI', 'MUSTERI_ADI', 'MASA_NUMARASI', 'ODEME_METODU']

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('siparis_goster')

class ExportPDF(View):
    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="siparisler.pdf"'

        p = canvas.Canvas(response, pagesize=letter)
        p.drawString(100, 750, "Siparişlər")
        
        siparisler = Siparis.objects.all()
        y_position = 730
        for siparis in siparisler:
            p.drawString(100, y_position, f"{siparis.MUSTERI_ADI}: {siparis.toplam_tutar} AZN")
            y_position -= 20

        p.showPage()
        p.save()
        return response
