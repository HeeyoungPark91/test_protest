# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 08:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1000)),
                ('account_number', models.PositiveIntegerField(default=1)),
                ('bank', models.CharField(choices=[('a', '신한은행'), ('b', '국민은행'), ('c', '하나은행'), ('d', '기업은행'), ('e', '농협은행')], default='a', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DonationState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Protest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of', models.CharField(choices=[('a', '집회'), ('b', '서명운동'), ('c', '전시'), ('d', '플래시몹'), ('e', '모금'), ('f', '기타')], default='a', max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('video', models.URLField(blank=True)),
                ('place', models.TextField(blank=True)),
                ('date', models.DateField(blank=True)),
                ('number_of_people', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='protest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protest.User'),
        ),
        migrations.AddField(
            model_name='participation',
            name='protest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protest.Protest'),
        ),
        migrations.AddField(
            model_name='participation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protest.User'),
        ),
        migrations.AddField(
            model_name='donationstate',
            name='protest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protest.Protest'),
        ),
        migrations.AddField(
            model_name='donationstate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protest.User'),
        ),
        migrations.AddField(
            model_name='donation',
            name='protest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protest.Protest'),
        ),
    ]
