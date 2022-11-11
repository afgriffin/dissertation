# Generated by Django 4.1.1 on 2022-09-27 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0014_alter_participant_soil_sample_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='participant',
            name='soil_sample_label',
            field=models.CharField(blank=True, editable=False, max_length=200, unique=True),
        ),
    ]