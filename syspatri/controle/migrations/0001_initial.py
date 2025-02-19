# Generated by Django 5.1 on 2025-02-19 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patrimonio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='Data de Início')),
                ('data_fim', models.DateField(blank=True, null=True, verbose_name='Data de Término')),
                ('custo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Custo')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Manutenção',
                'verbose_name_plural': 'Manutenções',
            },
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_movimentacao', models.DateTimeField(auto_now_add=True, verbose_name='Data da Movimentação')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
            },
        ),
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data da Auditoria')),
                ('observacao', models.TextField(verbose_name='Observação')),
                ('bem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.bem', verbose_name='Bem')),
            ],
            options={
                'verbose_name': 'Auditoria',
                'verbose_name_plural': 'Auditorias',
            },
        ),
    ]
