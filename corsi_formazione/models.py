from django.db import models

class Corso(models.Model):
    titolo = models.CharField(max_length = 20)
    descrizione = models.CharField(max_length = 20)
    dataInizio = models.DateField()
    dataFine = models.DateField()
    postiDisponibili = models.IntegerField()

    def __str__(self):
        return self.titolo + " " + self.descrizione + " " + self.dataInizio + " " + self.dataFine + " " + self.postiDisponibili

