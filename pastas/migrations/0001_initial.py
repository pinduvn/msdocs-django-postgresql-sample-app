# Generated by Django 4.1.5 on 2023-01-20 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre descriptivo', max_length=200, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'barrio',
                'verbose_name_plural': 'barrios',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre descriptivo', max_length=200, verbose_name='Nombre')),
                ('numero_documento', models.BigIntegerField(help_text='numero de documento / CUIT', null=True, verbose_name='numero documeto')),
                ('direccion', models.CharField(blank=True, help_text='dirección del cliente', max_length=200, null=True, verbose_name='dirección')),
                ('celular', models.BigIntegerField(blank=True, help_text='Número de celular con caracteristica del/la administrador/a', null=True, verbose_name='Celular')),
                ('telefono', models.BigIntegerField(blank=True, help_text='teléfono fijo', null=True, verbose_name='teléfono')),
                ('email', models.EmailField(blank=True, help_text='email del cliente', max_length=254, null=True, verbose_name='email')),
                ('barrio', models.ForeignKey(blank=True, help_text='barrio donde reside ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', to='pastas.barrio', verbose_name='barrio')),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre descriptivo', max_length=200, verbose_name='Nombre')),
                ('costo', models.DecimalField(decimal_places=2, default=0, help_text='Costo del ingrediente expresado en pesos', max_digits=15, verbose_name='Costo')),
            ],
            options={
                'verbose_name': 'Ingrediente',
                'verbose_name_plural': 'Ingredientes',
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre descriptivo', max_length=200, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'localidad',
                'verbose_name_plural': 'localidades',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre descriptivo', max_length=200, verbose_name='Nombre')),
                ('ganancia', models.DecimalField(decimal_places=2, default=0, help_text='Ganancia del producto, expresado en coeficiente.', max_digits=15, verbose_name='Ganancia')),
                ('es_relleno', models.BooleanField(default=False, help_text='Especifica si el producto contiene relleno.', verbose_name='Es Relleno')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre descriptivo', max_length=200, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'provincia',
                'verbose_name_plural': 'provincias',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre descriptivo', max_length=200, verbose_name='Nombre')),
            ],
            options={
                'ordering': ['nombre'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(help_text='fecha de la venta', verbose_name='fecha')),
                ('cliente', models.ForeignKey(help_text='cliente que realiza la compra', on_delete=django.db.models.deletion.PROTECT, related_name='compras', to='pastas.cliente', verbose_name='cliente')),
            ],
            options={
                'verbose_name': 'venta',
                'verbose_name_plural': 'ventas',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=3, default=0, help_text='Cantidad del ingrediente, expresado en su unidad de medida.', max_digits=15, verbose_name='Cantidad')),
                ('ingrediente', models.ForeignKey(help_text='Ingrediente de la receta', on_delete=django.db.models.deletion.PROTECT, related_name='recetas', to='pastas.ingrediente')),
                ('producto', models.ForeignKey(help_text='Producto de la receta', on_delete=django.db.models.deletion.PROTECT, related_name='recetas', to='pastas.producto')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['ingrediente'],
            },
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='unidad_medida',
            field=models.ForeignKey(default=1, help_text='Unidad de medida del ingrediente', on_delete=django.db.models.deletion.PROTECT, related_name='ingredientes', to='pastas.unidadmedida'),
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='cantidad', max_digits=15, null=True, verbose_name='cantidad')),
                ('producto', models.ForeignKey(help_text='producto', on_delete=django.db.models.deletion.PROTECT, related_name='detalle', to='pastas.producto', verbose_name='producto')),
                ('venta', models.ForeignKey(help_text='detalle de la compra', on_delete=django.db.models.deletion.PROTECT, related_name='detalle', to='pastas.venta', verbose_name='venta')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='localidad',
            field=models.ForeignKey(blank=True, help_text='localidad donde reside el cliente', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', to='pastas.localidad', verbose_name='localidad'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='provincia',
            field=models.ForeignKey(blank=True, help_text='provincia donde reside', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_related', to='pastas.provincia', verbose_name='provincia'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.ForeignKey(blank=True, help_text='Usuario con el que se loguea al sistema', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s', related_query_name='%(app_label)s_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
        migrations.AddIndex(
            model_name='cliente',
            index=models.Index(fields=['numero_documento', 'user'], name='pastas_cliente_unico'),
        ),
    ]
