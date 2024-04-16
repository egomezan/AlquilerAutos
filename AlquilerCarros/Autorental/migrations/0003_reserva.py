# Generated by Django 4.2.9 on 2024-04-16 01:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('autorental', '0002_remove_carro_descripcion_alter_carro_transmision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_usuario', models.CharField(max_length=50)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('hora_inicio', models.TimeField(default=django.utils.timezone.now)),
                ('hora_fin', models.TimeField(default=django.utils.timezone.now)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='autorental.carro')),
            ],
        ),
    ]
