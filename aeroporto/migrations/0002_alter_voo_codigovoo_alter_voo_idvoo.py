# Generated by Django 4.1.3 on 2022-11-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aeroporto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voo',
            name='codigoVoo',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='voo',
            name='idVoo',
            field=models.IntegerField(unique=True),
        ),
    ]