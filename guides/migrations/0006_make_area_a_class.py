# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-28 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0005_allow_controls_to_accept_a_blank_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='guide',
            name='language',
            field=models.ManyToManyField(to='guides.Language', verbose_name='What languages can you communicate in fluently?'),
        ),
        migrations.RemoveField(
            model_name='participant',
            name='areas',
        ),
        migrations.AddField(
            model_name='participant',
            name='areas',
            field=models.ManyToManyField(help_text='Further information about IETF areas is available <a href="https://www.ietf.org/topics/areas/">here</a>.', to='guides.Area', verbose_name='What IETF area(s) most interest you?'),
        ),
    ]
