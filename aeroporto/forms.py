from django import forms
from .models import Voo

class VooForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ('idVoo', 'codigoVoo', 'companhiaAerea', 'partidaPrevista', 'chegadaPrevista', 'rota', 'aeroportoOrigem', 'aeroportoDestino')
        
        widgets = {
            'idVoo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Insira o Id do Voo'}),
            'codigoVoo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Insira o Código do Voo'}),
            'companhiaAerea': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira a Companhia Aérea'}),
            'partidaPrevista': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Ano-Mês-Dia Hora:Minuto:Segundo'}),
            'chegadaPrevista': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Ano-Mês-Dia Hora:Minuto:Segundo'}),
            'rota': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira a Rota do voo'}),
            'aeroportoOrigem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o Aeroporto de Origem'}),
            'aeroportoDestino' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o Aeroporto de Destino'}),
            
        }
        
class VooEditForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ('codigoVoo', 'companhiaAerea', 'partidaPrevista', 'chegadaPrevista', 'rota', 'aeroportoOrigem', 'aeroportoDestino')
        
        widgets = {
            'codigoVoo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Insira o Código do Voo'}),
            'companhiaAerea': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira a Companhia Aérea'}),
            'partidaPrevista': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Ano-Mês-Dia Hora:Minuto:Segundo'}),
            'chegadaPrevista': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Ano-Mês-Dia Hora:Minuto:Segundo'}),
            'rota': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira a Rota do voo'}),
            'aeroportoOrigem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o Aeroporto de Origem'}),
            'aeroportoDestino' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o Aeroporto de Destino'}),
            
        }

