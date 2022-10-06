from django.test import TestCase
from aeroporto.models import Voo, Usuario
from datetime import datetime

# Create your tests here.
class VooModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Voo.objects.create(
            codigoVoo = 1234,
            companhiaAerea = 'LabSoft',
            partidaPrevista = datetime.strptime('10/06/22 14:00', '%d/%m/%y %H:%M'),
            chegadaPrevista = datetime.strptime('10/06/22 17:40', '%d/%m/%y %H:%M'),
            status = 'Aguardo',
            aeroportoOrigem = 'CGH',
            aeroportoDestino = 'BSB',
        )

        Voo.objects.create(
            codigoVoo = 5678,
            companhiaAerea = 'LabSoft',
            partidaPrevista = datetime.strptime('11/06/22 14:00', '%d/%m/%y %H:%M'),
            chegadaPrevista = datetime.strptime('11/06/22 17:40', '%d/%m/%y %H:%M'),
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
