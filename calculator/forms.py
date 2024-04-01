from django import forms

class ConsumptionForm(forms.Form):
    consumption1 = forms.FloatField(label='Consumption 1')
    consumption2 = forms.FloatField(label='Consumption 2')
    consumption3 = forms.FloatField(label='Consumption 3')
    distributor_tariff = forms.FloatField(label='Distributor Tariff')
    tariff_type = forms.ChoiceField(choices=[('residential', 'Residential'), ('commercial', 'Commercial'), ('industrial', 'Industrial')], label='Tariff Type')
