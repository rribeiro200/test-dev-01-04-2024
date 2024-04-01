# models.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models

class Tariff(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Nome'))
    description = models.TextField(verbose_name=_('Descrição'))
    discount_residential = models.FloatField(verbose_name=_('Desconto Residencial'))
    discount_commercial = models.FloatField(verbose_name=_('Desconto Comercial'))
    discount_industrial = models.FloatField(verbose_name=_('Desconto Industrial'))

    def __str__(self):
        return self.name

class Consumer(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Nome'))
    email = models.EmailField(max_length=100, verbose_name=_('E-mail'))
    address = models.CharField(max_length=255, verbose_name=_('Endereço'))
    cep = models.CharField(max_length=9)  # Adicionando o campo CEP
    consumption1 = models.FloatField(verbose_name=_('Consumo Mês 1 (kWh)'))
    consumption2 = models.FloatField(verbose_name=_('Consumo Mês 2 (kWh)'))
    consumption3 = models.FloatField(verbose_name=_('Consumo Mês 3 (kWh)'))
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, verbose_name=_('Tarifa'))

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.tariff.name == 'Residencial':
            self.validate_residential_consumption()
        elif self.tariff.name == 'Comercial':
            self.validate_commercial_consumption()
        elif self.tariff.name == 'Industrial':
            self.validate_industrial_consumption()

    def validate_residential_consumption(self):
        if self.consumption1 > 10000 or self.consumption2 > 10000 or self.consumption3 > 10000:
            raise ValidationError(_("O consumo para um consumidor residencial não pode exceder 10.000 kWh."))

    def validate_commercial_consumption(self):
        if self.consumption1 > 20000 or self.consumption2 > 20000 or self.consumption3 > 20000:
            raise ValidationError(_("O consumo para um consumidor comercial não pode exceder 20.000 kWh."))

    def validate_industrial_consumption(self):
        if self.consumption1 > 50000 or self.consumption2 > 50000 or self.consumption3 > 50000:
            raise ValidationError(_("O consumo para um consumidor industrial não pode exceder 50.000 kWh."))

    def save(self, *args, **kwargs):
        self.full_clean()  # Executar validações antes de salvar
        super().save(*args, **kwargs)