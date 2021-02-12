from django.db import models


class ProdutoIlicito(models.Model):
    PORCAO_CHOICES = (
        (1, '5 gramas'),
        (2, '10 gramas'),
        (3, '15 gramas'),
        (4, '25 gramas'),
        (5, '50 gramas')
    )
    nome = models.CharField(max_length=250)
    quantidade = models.IntegerField()
    porcao = models.SmallIntegerField(choices=PORCAO_CHOICES)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = "Produto Ilicito"
        verbose_name_plural = "Produtos Ilicitos"
        ordering = ['nome', 'quantidade']

    def __str__(self):
        return self.nome
