from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=20, verbose_name="Nome Categoria", blank=False)
    descrizione = models.TextField(verbose_name="Descrizione", blank=False)

    def __str__(self):
        return self.nome_categoria

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"

class ContoCorrente(models.Model):
    nome_conto_corrente = models.CharField(max_length=20, verbose_name="Nome Conto Corrente", blank=False)
    banca = models.CharField(max_length=20, verbose_name="Banca", blank=False)

    def __str__(self):
        return self.nome_conto_corrente

    class Meta:
        verbose_name = "Conto Corrente"
        verbose_name_plural = "Conti Correnti"

class CentroDiCosto(models.Model):
    nome_centro_di_costo = models.CharField(max_length=20, verbose_name="Nome Centro di Costo", blank=False)
    mese = models.CharField(max_length=20, verbose_name="Mese", blank=False)
    importo_centro_di_costo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Importo Centro di Costo", blank=False)

    def __str__(self):
        return self.nome_centro_di_costo

    class Meta:
        verbose_name = "Centro di Costo"
        verbose_name_plural = "Centri di Costo"

class SpesaFissa(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    conto_corrente = models.ForeignKey(ContoCorrente, on_delete=models.CASCADE, verbose_name="Conto Corrente")
    centro_di_costo = models.ForeignKey(CentroDiCosto, on_delete=models.CASCADE, verbose_name="Centro di Costo")
    oggetto_spesa_fissa= models.CharField(max_length=20, verbose_name="Oggetto spesa fissa", blank=False)
    importo_spesa_fissa = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Importo Spesa Fissa", blank=False)
    data_disattivazione = models.DateField(verbose_name="DataDisattivazione")

    def __str__(self):
        return f"{self.data_disattivazione} - {self.categoria} - {self.oggetto_spesa_fissa} - {self.importo_spesa_fissa}€"

    class Meta:
        verbose_name = "Spesa Fissa"
        verbose_name_plural = "Spese Fisse"  

class Transazione(models.Model):
    data = models.DateField(verbose_name="Data", blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    conto_corrente = models.ForeignKey(ContoCorrente, on_delete=models.CASCADE, verbose_name="Conto Corrente")
    centro_di_costo = models.ForeignKey(CentroDiCosto, on_delete=models.CASCADE, verbose_name="Centro di Costo")
    oggetto_spesa= models.CharField(max_length=20, verbose_name="Oggetto Spesa", blank=False)
    importo_transazione = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Importo Transazione", blank=False)

    def __str__(self):
        return f"{self.data} - {self.categoria} - {self.oggetto_spesa} - {self.importo_transazione}€"

    class Meta:
        verbose_name = "Transazione"
        verbose_name_plural = "Transazioni"



