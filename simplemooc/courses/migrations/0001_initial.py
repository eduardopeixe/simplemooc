# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Shortcut')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('start_date', models.DateField(verbose_name='Start Date', null=True, blank=True)),
                ('image', models.ImageField(upload_to='courses/images', verbose_name='Image', null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
    ]
