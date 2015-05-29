# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('ganador', models.ForeignKey(related_name='partidos_ganados', to='partidos.Equipo')),
                ('local', models.ForeignKey(related_name='partidos_como_local', to='partidos.Equipo')),
                ('visitante', models.ForeignKey(related_name='partidos_como_visitante', to='partidos.Equipo')),
            ],
        ),
    ]
