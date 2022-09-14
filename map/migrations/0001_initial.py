# Generated by Django 4.1.1 on 2022-09-14 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participants', '0014_alter_participant_soil_sample_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapCoordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('participant', models.OneToOneField(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='result', to='participants.participant')),
            ],
        ),
    ]