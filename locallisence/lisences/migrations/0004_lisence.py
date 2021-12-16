# Generated by Django 4.0 on 2021-12-14 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lisences', '0003_rename_clientes_client_rename_productos_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lisence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=100)),
                ('Compañía_ERP', models.CharField(max_length=100)),
                ('Estado', models.CharField(choices=[('InActiva', 'InActiva'), ('Vigente', 'Vigente'), ('Vencida', 'Vencida')], max_length=50)),
                ('Fecha_de_inicio', models.DateField(verbose_name='Fecha de inicio')),
                ('Fecha_de_fin', models.DateField(verbose_name='Fecha de fin')),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lisences.client')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lisences.product')),
            ],
        ),
    ]