from django import forms
from .models import Voo

# Variáveis de opções de escolha do forms para criação do voo
choices = [('Partindo', 'Partindo'), ('Chegando', 'Chegando')]


# Forms para criação e atualização do voo - CRUD
class VooForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ('codigoVoo', 'companhiaAerea', 'partidaPrevista', 'chegadaPrevista', 'rota', 'aeroportoOrigem', 'aeroportoDestino', 'condicao')
        
        widgets = {
            'codigoVoo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Insira o Código do Voo'}),
            'companhiaAerea': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira a Companhia Aérea'}),
            'partidaPrevista': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Ano-Mês-Dia Hora:Minuto:Segundo'}),
            'chegadaPrevista': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Ano-Mês-Dia Hora:Minuto:Segundo'}),
            'rota': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira a Rota do voo'}),
            'aeroportoOrigem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o Aeroporto de Origem'}),
            'aeroportoDestino': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o Aeroporto de Destino'}),
            'condicao': forms.Select(choices=choices, attrs={'class': 'form-control', 'placeholder': 'Condição do Voo'}),
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


# Forms para atualização do voo - Monitoramento
class VooUpdateStatusForm(forms.ModelForm):
    def __init__(self, choices=None, *args, **kwargs):
        super(VooUpdateStatusForm, self).__init__(*args, **kwargs)
        self.fields['status'].choices = choices
        self.fields['status'].widget.choices = choices
    class Meta:
        model = Voo
        fields = ('status',)
        status = forms.Select(choices=[()], attrs={'class': 'form-control', 'placeholder': 'Insira o status atual do voo'})
        widgets = {
            'status': forms.Select(choices=[()], attrs={'class': 'form-control', 'placeholder': 'Insira o status atual do voo'}),
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


# Forms para geração dos relatórios - Relatório
class VooReportForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ('companhiaAerea',)

        widgets = {
            'companhiaAerea': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira a Companhia Aérea'}),
        }
