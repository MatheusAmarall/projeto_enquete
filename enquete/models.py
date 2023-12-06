from django.db import models
from django.contrib.auth.models import User

class Enquetes(models.Model):
    pergunta = models.TextField()
    opcao_um = models.CharField(max_length=30)
    opcao_dois = models.CharField(max_length=30)
    opcao_tres = models.CharField(max_length=30)
    opcao_quatro = models.CharField(max_length=30)
    qtd_opcao_um = models.IntegerField(default=0)
    qtd_opcao_dois = models.IntegerField(default=0)
    qtd_opcao_tres = models.IntegerField(default=0)
    qtd_opcao_quatro = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enquete_aberta = models.BooleanField(default=True)

    def total(self):
        return self.qtd_opcao_um + self.qtd_opcao_dois + self.qtd_opcao_tres + self.qtd_opcao_quatro
    
    def __str__(self):
        return self.pergunta
    
    class Meta:
        verbose_name = 'Enquete'
        verbose_name_plural = 'Enquetes'

class VotacoesEnquetes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enquete = models.ForeignKey(Enquetes, on_delete=models.CASCADE)

    def __str__(self):
        return self.enquete.pergunta
    
    class Meta:
        verbose_name = 'VotacaoEnquete'
        verbose_name_plural = 'VotacoesEnquetes'