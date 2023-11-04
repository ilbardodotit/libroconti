from django.contrib import admin
from .models import Categoria, ContoCorrente, CentroDiCosto, Transazione, SpesaFissa

# Registra i modelli per renderli visibili nell'interfaccia di amministrazione
admin.site.register(Categoria)
admin.site.register(ContoCorrente)
admin.site.register(CentroDiCosto)
admin.site.register(SpesaFissa)
admin.site.register(Transazione)
