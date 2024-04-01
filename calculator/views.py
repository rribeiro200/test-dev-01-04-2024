from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View
from .models import Consumer, Tariff
from calculator_python import ResidentialTariff, CommercialTariff, IndustrialTariff, DiscountContext

class CalculateElectricitySavings(View):
    def post(self, request):
        try:
            consumption1 = float(request.POST.get('consumption1'))
            consumption2 = float(request.POST.get('consumption2'))
            consumption3 = float(request.POST.get('consumption3'))
            tariff_id = int(request.POST.get('tariff_type'))
        except (ValueError, TypeError):
            return render(request, 'calculator/error.html', {'error_message': 'Dados inválidos no formulário.'})

        try:
            tariff = Tariff.objects.get(pk=tariff_id)
        except Tariff.DoesNotExist:
            return render(request, 'calculator/error.html', {'error_message': 'Tarifa não encontrada.'})

        if tariff.name == 'Residencial':
            tariff_strategy = ResidentialTariff()
        elif tariff.name == 'Comercial':
            tariff_strategy = CommercialTariff()
        elif tariff.name == 'Industrial':
            tariff_strategy = IndustrialTariff()
        else:
            return render(request, 'calculator/error.html', {'error_message': 'Tipo de tarifa inválido.'})

        try:
            consumer = Consumer.objects.create(
                consumption1=consumption1,
                consumption2=consumption2,
                consumption3=consumption3,
                tariff=tariff
            )
        except Exception as e:
            return render(request, 'calculator/error.html', {'error_message': str(e)})

        discount_context = DiscountContext(tariff_strategy)
        discount = discount_context.apply_discount(sum([consumption1, consumption2, consumption3]))
        coverage = discount_context.calculate_coverage(sum([consumption1, consumption2, consumption3]))

        return render(request, 'calculator/results.html', {'discount': discount, 'coverage': coverage})

    def get(self, request):
        # Lógica de filtragem e renderização do formulário com a lista de consumidores
        tariffs = Tariff.objects.all()

        # Obter os parâmetros de filtro, se existirem
        consumer_type = request.GET.get('consumer_type')
        consumption_range = request.GET.get('consumption_range')

        # Filtrar os consumidores com base nos parâmetros
        consumers = Consumer.objects.all()

        if consumer_type:
            consumers = consumers.filter(tariff__name=consumer_type)

        if consumption_range:
            min_consumption, max_consumption = map(int, consumption_range.split('-'))
            consumers = consumers.filter(Q(consumption1__range=(min_consumption, max_consumption)) |
                                         Q(consumption2__range=(min_consumption, max_consumption)) |
                                         Q(consumption3__range=(min_consumption, max_consumption)))

        return render(request, 'calculator/calculator.html', {'tariffs': tariffs, 'consumers': consumers})

class AddConsumer(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        consumption1 = float(request.POST.get('consumption1'))
        consumption2 = float(request.POST.get('consumption2'))
        consumption3 = float(request.POST.get('consumption3'))
        tariff_id = int(request.POST.get('tariff_type'))

        try:
            tariff = Tariff.objects.get(pk=tariff_id)
        except Tariff.DoesNotExist:
            return render(request, 'calculator/error.html', {'error_message': 'Tarifa não encontrada.'})

        if tariff.name == 'Residencial':
            tariff_strategy = ResidentialTariff()
        elif tariff.name == 'Comercial':
            tariff_strategy = CommercialTariff()
        elif tariff.name == 'Industrial':
            tariff_strategy = IndustrialTariff()
        else:
            return render(request, 'calculator/error.html', {'error_message': 'Tipo de tarifa inválido.'})

        try:
            consumer = Consumer.objects.create(
                name=name,
                email=email,
                address=address,
                cep=cep,
                consumption1=consumption1,
                consumption2=consumption2,
                consumption3=consumption3,
                tariff=tariff
            )
        except Exception as e:
            return render(request, 'calculator/error.html', {'error_message': str(e)})

        return redirect('calculator:calculator')

    def get(self, request):
        # Obter os parâmetros de filtro
        consumer_type = request.GET.get('consumer_type')
        consumption_range = request.GET.get('consumption_range')

        # Filtrar os consumidores de acordo com os parâmetros
        consumers = Consumer.objects.all()

        if consumer_type and consumer_type != 'Todos':
            consumers = consumers.filter(tariff__name=consumer_type)

        if consumption_range and consumption_range != 'Todos':
            min_consumption, max_consumption = map(int, consumption_range.split('-'))
            consumers = consumers.filter(Q(consumption1__range=(min_consumption, max_consumption)) |
                                         Q(consumption2__range=(min_consumption, max_consumption)) |
                                         Q(consumption3__range=(min_consumption, max_consumption)))

        tariffs = Tariff.objects.all()

        # Renderizar o template com os consumidores filtrados
        return render(request, 'calculator/add_consumer.html', {'consumers': consumers, 'tariffs': tariffs})
