# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pollster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('base_url', models.URLField()),
                ('poll_regex', models.CharField(max_length=255)),
                ('pdf_regex', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('has_subquestions', models.BinaryField()),
                ('poll', models.ForeignKey(to='Poll.Poll')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subquestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('question', models.ForeignKey(to='Poll.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='poll',
            name='pollster',
            field=models.ForeignKey(to='Poll.Pollster'),
            preserve_default=True,
        ),
    ]
