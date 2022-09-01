# Generated by Django 4.1 on 2022-09-01 10:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0010_alter_participant_sample_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(default='Please enter your email address', max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='sample_label',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='participant',
            name='soil_sample_label',
            field=models.CharField(blank=True, editable=False, max_length=200),
        ),
    ]
