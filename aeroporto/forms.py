from django import forms
from .models import Voo

choices = [('Embarcando', 'Embarcando'), ('Cancelado', 'Cancelado'), ('Programado', 'Programado'), ('Taxiando', 'Taxiando'), 
         ('Pronto', 'Pronto'), ('Autorizado', 'Autorizado'), ('Em voo', 'Em voo'), ('Aterrissado', 'Aterrissado')]

class VooForm(forms.ModelForm):
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

class VooUpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ('status',)
        
        widgets = {
            'status': forms.Select(choices=choices, attrs={'class': 'form-control', 'placeholder': 'Insira o status atual do voo'}),
        }
        
class VooUpdateDepartureForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ('partidaReal',)
        
        widgets = {
            'partidaReal': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Ano-Mês-Dia Hora:Minuto:Segundo'}),
        }
        
class VooUpdateArrivalForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ('chegadaReal',)
        
        widgets = {
            'chegadaReal': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Ano-Mês-Dia Hora:Minuto:Segundo'}),
        }
        
class VooReportForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ('companhiaAerea',)
        
        widgets = {
            'companhiaAerea': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira a Companhia Aérea'}),
        }