from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, verbose_name="E-mail")
    senha = models.SlugField(max_length=30)
    nascimento = models.DateField(
        auto_now=False, auto_now_add=False)
    endereco = models.CharField(max_length=30, verbose_name="Endereço")
    cep = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.nome, self.email)