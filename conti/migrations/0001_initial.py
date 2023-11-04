# Generated by Django 4.2.7 on 2023-11-02 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=20, verbose_name='Nome Categoria')),
                ('descrizione', models.TextField(verbose_name='Descrizione')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorie',
            },
        ),
        migrations.CreateModel(
            name='CentroDiCosto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_centro_di_costo', models.CharField(max_length=20, verbose_name='Nome Centro di Costo')),
                ('mese', models.CharField(max_length=20, verbose_name='Mese')),
                ('importo_centro_di_costo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Importo Centro di Costo')),
            ],
            options={
                'verbose_name': 'Centro di Costo',
                'verbose_name_plural': 'Centri di Costo',
            },
        ),
        migrations.CreateModel(
            name='ContoCorrente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_conto_corrente', models.CharField(max_length=20, verbose_name='Nome Conto Corrente')),
                ('banca', models.CharField(max_length=20, verbose_name='Banca')),
            ],
            options={
                'verbose_name': 'Conto Corrente',
                'verbose_name_plural': 'Conti Correnti',
            },
        ),
        migrations.CreateModel(
            name='Transazione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('oggetto_spesa', models.CharField(max_length=20, verbose_name='Oggetto Spesa')),
                ('importo_transazione', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Importo Transazione')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conti.categoria', verbose_name='Categoria')),
                ('centro_di_costo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conti.centrodicosto', verbose_name='Centro di Costo')),
                ('conto_corrente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conti.contocorrente', verbose_name='Conto Corrente')),
            ],
            options={
                'verbose_name': 'Transazione',
                'verbose_name_plural': 'Transazioni',
            },
        ),
        migrations.CreateModel(
            name='SpesaFissa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oggetto_spesa_fissa', models.CharField(max_length=20, verbose_name='Oggetto spesa fissa')),
                ('importo_spesa_fissa', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Importo Spesa Fissa')),
                ('data_disattivazione', models.DateField(verbose_name='DataDisattivazione')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conti.categoria', verbose_name='Categoria')),
                ('centro_di_costo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conti.centrodicosto', verbose_name='Centro di Costo')),
                ('conto_corrente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conti.contocorrente', verbose_name='Conto Corrente')),
            ],
            options={
                'verbose_name': 'Spesa Fissa',
                'verbose_name_plural': 'Spese Fisse',
            },
        ),
    ]