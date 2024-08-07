# Generated by Django 5.0.6 on 2024-07-22 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reserva',
            new_name='ReservaSemanal',
        ),
        migrations.CreateModel(
            name='ReservaDiaUnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diaHoraInicio', models.DateTimeField(auto_now=True)),
                ('diaHoraFim', models.DateTimeField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.local')),
                ('matResponsavel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.usuario')),
                ('matSolicitante', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_usuario', to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ReservaMensal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias', models.JSONField()),
                ('meses', models.IntegerField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.local')),
                ('matResponsavel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.usuario')),
                ('matSolicitante', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_usuario', to='app.usuario')),
            ],
        ),
    ]