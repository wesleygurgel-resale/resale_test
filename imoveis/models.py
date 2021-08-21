from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Imobiliaria(Base):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Imobiliaria'
        verbose_name_plural = 'Imobiliarias'
        unique_together = ['nome', 'endereco']
        ordering = ['id']

    def __str__(self):
        return self.nome


class Imovel(Base):
    TIPO_IMOVEL = [
        ('Apartamento', 'Apartamento'),
        ('Casa', 'Casa'),
    ]

    FINALIDADE_IMOVEL = [
        ('Residencial', 'Residencial'),
        ('Escritorio', 'Escritorio'),
    ]

    imobiliaria = models.ForeignKey(Imobiliaria, related_name='propriedades', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, choices=TIPO_IMOVEL, default='Apartamento')
    finalidade = models.CharField(max_length=255, choices=FINALIDADE_IMOVEL, default='Residencial')

    descricao = models.TextField(default='Ainda não foi criada uma descrição para este Imóvel')
    caracteristica = models.TextField(blank=True, default='Características ainda não foram especificadas para este '
                                                          'Imóvel!')

    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'
        unique_together = ['nome', 'endereco']
        ordering = ['id']

    def __str__(self):
        return f'O imóvel {self.nome} localizado em {self.endereco} está sobre responsabilidade da(o) {self.imobiliaria}'
