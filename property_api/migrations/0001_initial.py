# Generated by Django 4.1.4 on 2022-12-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CKANResource',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('suffix', models.CharField(max_length=7)),
                ('resource_id', models.CharField(default=None, max_length=40, verbose_name='Resource ID')),
                ('parcel_id_field', models.CharField(max_length=200, verbose_name='Parcel ID field (e.g. PARID)')),
                ('multi_per_pin', models.BooleanField(verbose_name='Parcel can have multiple records')),
                ('info', models.CharField(max_length=400)),
                ('has_geo', models.BooleanField(help_text='Should only be for one resource.', verbose_name='Contains coordinates')),
                ('lat_field', models.CharField(blank=True, help_text='Only if field contains coordinates', max_length=20)),
                ('lon_field', models.CharField(blank=True, help_text='Only if field contains coordinates', max_length=20)),
            ],
            options={
                'verbose_name': 'CKAN Resource',
            },
        ),
    ]