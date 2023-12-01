from django.db import models

# Create your models here.


class Documento(models.Model):
    descricao = models.CharField(max_length=100)

    def _str_(self):
        return self.descricao
