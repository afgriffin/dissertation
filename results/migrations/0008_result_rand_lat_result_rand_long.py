# Generated by Django 4.1.1 on 2022-09-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0007_result_latitude_result_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='rand_lat',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='result',
            name='rand_long',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]