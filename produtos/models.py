from django.db import models
from .utils import pegar_dados


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    url = models.URLField()
    preco_atual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    preco_original = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(null=True, blank=True)
    imagem_url = models.URLField(null=True, blank=True)

    def adicionar_produto(self):
        resultado = pegar_dados(self.url)
        if resultado:
            self.nome = resultado["titulo"]
            self.preco_original = resultado["preco"]
            self.preco_atual = resultado["preco"]
            self.imagem_url = resultado["imagem"]
            self.save()
            return resultado

    def atualizar_dados(self):
        resultado = pegar_dados(self.url)
        if resultado:
            self.nome = resultado["titulo"]
            self.preco_atual = resultado["preco"]
            self.imagem_url = resultado["imagem"]
            self.save()
            return resultado
        return None

    def __str__(self):
        return self.nome