# Generated by Django 4.1 on 2022-08-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0003_alter_participant_agreement'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='veg_species_other',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='participant',
            name='bumblebee',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='butterfly',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='contact_preference',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='participant',
            name='domestic_cat',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='frog',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='goldfinch',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='hedgehog',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='house_rat',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='house_sparrow',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='ladybird',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='mole',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='red_fox',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='robin',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='slow_worm',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='wren',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('seasonally', 'Seasonally'), ('yearly', 'Yearly'), ('never', 'Never'), ('unknown', 'Unknown')], default='daily', max_length=20),
        ),
    ]