# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nam', models.CharField(default=b'', max_length=100)),
            ],
            options={
                'db_table': 'car_model',
            },
            bases=(models.Model,),
        ),
    ]
