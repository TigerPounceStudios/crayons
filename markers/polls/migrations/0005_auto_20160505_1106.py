# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
            ],
        ),
        migrations.RemoveField(
            model_name='response',
            name='poll',
        ),
        migrations.AddField(
            model_name='response',
            name='response',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.PollChoices'),
            preserve_default=False,
        ),
    ]