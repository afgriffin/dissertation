# Generated by Django 4.1 on 2022-08-31 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('participants', '0007_participant_email_alter_participant_sample_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='soil_sample_label',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='participant',
            name='sample_label',
            field=models.CharField(default='A163B', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant', to=settings.AUTH_USER_MODEL),
        ),
    ]