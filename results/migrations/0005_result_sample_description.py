# Generated by Django 4.1 on 2022-09-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_rename_name_result_sample_label_alter_result_as_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='sample_description',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
