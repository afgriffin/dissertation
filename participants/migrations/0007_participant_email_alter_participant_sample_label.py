# Generated by Django 4.1 on 2022-08-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0006_alter_participant_sample_label_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='email',
            field=models.EmailField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='sample_label',
            field=models.CharField(default='12C21', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]