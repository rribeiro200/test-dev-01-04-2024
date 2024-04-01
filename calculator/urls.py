from django.urls import path, include
from . import views

app_name = 'calculator'

urlpatterns = [
    path('', views.CalculateElectricitySavings.as_view(), name='calculator'),
    path('add/', views.AddConsumer.as_view(), name='add_consumer'),
]
