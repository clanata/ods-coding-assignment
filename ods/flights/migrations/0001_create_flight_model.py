# Generated by Django 3.2.13 on 2022-06-16 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_id', models.CharField(max_length=6, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Created')),
                ('updated_at', models.DateTimeField(verbose_name='Updated')),
                ('flight_identifier', models.CharField(max_length=36, verbose_name='Flight Identifier')),
                ('flt_num', models.CharField(max_length=4, verbose_name='Flight Number')),
                ('scheduled_origin_gate', models.CharField(max_length=3, verbose_name='Origin Gate')),
                ('scheduled_destination_gate', models.CharField(max_length=3, verbose_name='Destination Gate')),
                ('out_gmt', models.DateTimeField(verbose_name='Departure')),
                ('in_gmt', models.DateTimeField(verbose_name='Arrival')),
                ('off_gmt', models.DateTimeField(verbose_name='Take-Off')),
                ('on_gmt', models.DateTimeField(verbose_name='Landing')),
                ('destination', models.CharField(max_length=3, verbose_name='Destination Code')),
                ('origin', models.CharField(max_length=3, verbose_name='Origin Code')),
                ('destination_full_name', models.CharField(max_length=64, verbose_name='Destination Full Name')),
                ('origin_full_name', models.CharField(max_length=64, verbose_name='Origin Full Name')),
            ],
        ),
    ]
