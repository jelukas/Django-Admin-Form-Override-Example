# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='ganador',
            field=models.ForeignKey(related_name='partidos_ganados', blank=True, to='partidos.Equipo', null=True),
        ),
    ]
