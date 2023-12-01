from django.db import models

# Create your models here.


class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return super.nome
