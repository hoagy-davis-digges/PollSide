# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('question', models.ForeignKey(to='Poll.Question', null=True)),
                ('subquestion', models.ForeignKey(to='Poll.Subquestion', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='Poll.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(null=True)),
                ('percentage', models.IntegerField()),
                ('answer', models.ForeignKey(to='Poll.Answer')),
                ('group', models.ForeignKey(to='Poll.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='name',
            new_name='heading',
        ),
        migrations.RemoveField(
            model_name='question',
            name='has_subquestions',
        ),
        migrations.AddField(
            model_name='poll',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 9, 22, 21, 34, 23, 11385)),
            preserve_default=True,
        ),
    ]
