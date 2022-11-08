from django.test import TestCase, Client
from django.http import HttpRequest
from aeroporto.models import Voo, Usuario
from aeroporto.forms import *
from datetime import datetime
from django.utils.timezone import make_aware

# Create your tests here.
class VooModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Voo.objects.create(
            codigoVoo = 1234,
            companhiaAerea = 'LabSoft',
            partidaPrevista = make_aware(datetime.strptime('01/11/22 14:00', '%d/%m/%y %H:%M')),
            chegadaPrevista = make_aware(datetime.strptime('01/11/22 17:40', '%d/%m/%y %H:%M')),
            status = 'Aguardo',
            aeroportoOrigem = 'CGH',
            aeroportoDestino = 'BSB',
        )

        Voo.objects.create(
            codigoVoo = 5678,
            companhiaAerea = 'LabSoft',
            partidaPrevista = make_aware(datetime.strptime('01/11/22 14:00', '%d/%m/%y %H:%M')),
            chegadaPrevista = make_aware(datetime.strptime('01/11/22 17:40', '%d/%m/%y %H:%M')),
            status = 'Aguardo',
            aeroportoOrigem = 'CGH',
            aeroportoDestino = 'BSB',
        )

    def test_criacao_id(self):
        Voo_1 = Voo.objects.get(codigoVoo=1234)
        Voo_2 = Voo.objects.get(codigoVoo=5678)
        self.assertEqual(Voo_1.idVoo, 1)
        self.assertEqual(Voo_2.idVoo, 2)
        self.assertFalse(Voo_1.idVoo == Voo_2.idVoo)
    
    def test_update(self):
        Voo_1 = Voo.objects.get(codigoVoo=1234)
        Voo_1.partidaReal = make_aware(datetime.strptime('01/11/22 14:30', '%d/%m/%y %H:%M'))
        Voo_1.save()
        
        Voo_1 = Voo.objects.get(codigoVoo=1234)
        self.assertEqual(Voo_1.partidaReal, datetime.strptime('01/11/22 14:30', '%d/%m/%y %H:%M'))
    
    def test_delete(self):
        pre_length = len(Voo.objects.all())
        Voo.objects.first().delete()
        self.assertEqual(pre_length, pre_length-1)


class UsuarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(
            nome = 'Sophia Asakura Lie',
            cargo = 'Comissário de Bordo',
            companhiaAerea = 'LabSoft',
            aeroportoTrabalho = 'CGH',
        )

    def test_criacao_id(self):
        usuario_1 = Usuario.objects.get(nome="Sophia Asakura Lie")
        self.assertEqual(usuario_1.idUsuario, 1)
        
    def test_update(self):
        Usuario_1 = Usuario.objects.get(nome="Sophia Asakura Lie")
        Usuario_1.aeroportoTrabalho = 'BSB'
        Usuario_1.save()
        
        Usuario_1 = Usuario.objects.get(nome="Sophia Asakura Lie")
        self.assertEqual(Usuario_1.aeroportoTrabalho, 'BSB')
    
    def test_delete(self):
        pre_length = len(Usuario.objects.all())
        Usuario.objects.first().delete()
        self.assertEqual(pre_length, pre_length-1)


# class CrudViewTest(TestCase):
#     client = Client()
    
#     @classmethod
#     def setUpTestData(cls):
#         Voo.objects.create(
#             idVoo = 1234,
#             codigoVoo = 1234,
#             companhiaAerea = 'LabSoft',
#             partidaPrevista = make_aware(datetime.strptime('01/11/22 14:00', '%d/%m/%y %H:%M')),
#             chegadaPrevista = make_aware(datetime.strptime('01/11/22 17:40', '%d/%m/%y %H:%M')),
#             rota = 'nenhuma',
#             status = 'Aguardo',
#             aeroportoOrigem = 'CGH',
#             aeroportoDestino = 'BSB',
#         )
    
#     def test_adicionar_voo(self):
#         voo_data = {
#             'idVoo': 1234,
#             'codigoVoo': 1234,
#             'companhiaAerea': 'LabSoft',
#             'partidaPrevista': '2022-11-01 14:00:00',
#             'chegadaPrevista': '2022-11-01 18:00:00',
#             'rota': 'nenhuma',
#             'aeroportoOrigem': 'CGH',
#             'aeroportoDestino': 'GRU'
#         }
        
#         response = self.client.post(
#             '/crud/adicionar_voo/',
#             voo_data,
#             content_type='application/x-www-form-urlencoded'
#         )
        
#         if response.status_code == 200:
#             Voo_object = Voo.objects.get(codigoVoo=1234)
        
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(Voo_object.codigoVoo, 1234)
    
#     def test_editar_voo(self):
#         voo_data = {
#             'codigoVoo': 76,
#             'companhiaAerea': 'LabSoft',
#             'partidaPrevista': '2022-11-01 14:00:00',
#             'chegadaPrevista': '2022-11-01 18:00:00',
#             'rota': 'alguma',
#             'aeroportoOrigem': 'CGH',
#             'aeroportoDestino': 'GRU'
#         }
        
#         response_get = self.client.get('/crud/editar_voo/1234')
#         if response_get.status_code == 200:
#             response_post = self.client.post('/crud/editar_voo/1234', voo_data)
        
#         request = HttpRequest()
#         request.POST = voo_data
#         form = VooEditForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else: print(form.errors)
#         print(form.is_valid())
            
#         self.assertEqual(response_post.status_code, 200)
    
#     def test_excluir_voo(self):
#         pass


class MonitoramentoViewTest(TestCase):
    client = Client()
    
    @classmethod
    def setUpTestData(cls):
        Voo.objects.create(
            codigoVoo = 1234,
            companhiaAerea = 'LabSoft',
            partidaPrevista = make_aware(datetime.strptime('01/11/22 14:00', '%d/%m/%y %H:%M')),
            chegadaPrevista = make_aware(datetime.strptime('01/11/22 17:40', '%d/%m/%y %H:%M')),
            status = 'Aguardo',
            aeroportoOrigem = 'CGH',
            aeroportoDestino = 'BSB',
        )

    def test_monitoramento(self):
        response = self.client.get('/monitoramento/?voo=1234')
        if response.status_code == 200:
            Voo_object = response.context['voo']
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Voo_object.codigoVoo, 1234)
        