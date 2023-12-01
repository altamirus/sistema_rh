from django.db import models

# Create your models here.


class HoraExtra(models.Model):
    motivo = models.CharField(max_length=100)

    def _str_(self):
        return self.motivo
