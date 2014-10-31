# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('phone', models.CharField(max_length=11)),
                ('description', models.TextField()),
                ('website', models.CharField(default=b'', max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('logo', django_resized.forms.ResizedImageField(default=b'company_directory/none/no-img.jpg', upload_to=b'company_directory/')),
                ('zip', models.CharField(max_length=5)),
                ('founded', models.PositiveSmallIntegerField()),
                ('capital', models.IntegerField()),
                ('date_modified', models.DateTimeField(default=datetime.datetime.now, auto_now=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(default=b'', unique=True, max_length=2)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.ForeignKey(to='company_directory.State'),
            preserve_default=True,
        ),
    ]
