# Generated by Django 4.0.2 on 2022-02-18 12:58

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polygon',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('geo_info', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('provider',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='polygons',
                                   to='provider.provider')),
            ],
        ),
    ]
