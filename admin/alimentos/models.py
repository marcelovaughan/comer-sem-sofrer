from datetime import timezone
import datetime
from django.db import models
from django.contrib.auth.models import User


class Alimento(models.Model):
    categoria = models.CharField(max_length=100, null=False)
    numeroAlimento = models.CharField(max_length=10, null=False)
    descricaoAlimento = models.CharField(max_length=255, null=False) 
    umidade = models.CharField(max_length=40, null=False)
    energiaKcal = models.CharField(max_length=40, null=False)
    energiaKj = models.CharField(max_length=40, null=False)
    proteina = models.CharField(max_length=40, null=False)
    lipideos = models.CharField(max_length=40, null=False)
    colesterol = models.CharField(max_length=40, null=False)
    carboidrato = models.CharField(max_length=40, null=False)
    fibraAlimentar = models.CharField(max_length=40, null=False)
    cinzas = models.CharField(max_length=40, null=False)
    calcio = models.CharField(max_length=40, null=False)
    magnesio = models.CharField(max_length=40, null=False)
    manganes = models.CharField(max_length=40, null=False)
    fosforo = models.CharField(max_length=40, null=False)
    ferro = models.CharField(max_length=40, null=False)
    sodio = models.CharField(max_length=40, null=False)
    potassio = models.CharField(max_length=40, null=False)
    cobre = models.CharField(max_length=40, null=False)
    zinco = models.CharField(max_length=40, null=False)
    retinol = models.CharField(max_length=40, null=False)
    re = models.CharField(max_length=40, null=False)
    rae = models.CharField(max_length=40, null=False)
    tiamina = models.CharField(max_length=40, null=False)
    riboflavina = models.CharField(max_length=40, null=False)
    piridoxina = models.CharField(max_length=40, null=False)
    niacina = models.CharField(max_length=40, null=False)
    vitaminaC = models.CharField(max_length=40, null=False)
    created_at = models.CharField(max_length=30, null=False)
    updated_at = models.CharField(max_length=30, null=False)

    def __str__(self):
        return '{}'.format(self.descricaoAlimento)
    

HORARIOS_REFEICOES_CHOICES = (
    ("1", "A PARTIR DAS 7:00 - CAFÉ DA MANHÃ"),
    ("2", "DAS 10:00 ÀS 11:00 - LANCHE DA MANHÃ"),
    ("3", "A PARTIR DAS 13:00 - ALMOÇO"),
    ("4", "ENTRE 16:00 E 17:00 - LANCHE DA TARDE"),
    ("5", "ATÉ ÀS 21:00 - JANTAR")
)


class Refeicao(models.Model):
    nome = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    horario = models.CharField(max_length=50, choices=HORARIOS_REFEICOES_CHOICES, null=False, default="1")
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    updated_at = models.DateTimeField(null=True, default=None, blank=True)

    class Meta:
        verbose_name_plural = "Refeições"

    def __str__(self):
        return '{}'.format(self.nome)
    
    def save(self, *args, **kwargs):        
        self.updated_at = datetime.datetime.now()
        super(Refeicao, self).save(*args, **kwargs)



class Porcao(models.Model):
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE, null=False)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, null=False)
    quantidade = models.IntegerField(null=False)
    unidade_medida = models.CharField(max_length=100, null=False, default="g")

    class Meta:
        verbose_name_plural = "Porções"
