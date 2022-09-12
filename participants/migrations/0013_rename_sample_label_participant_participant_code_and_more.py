# Generated by Django 4.1 on 2022-09-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0012_participant_postcode_participant_year_property_built'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='sample_label',
            new_name='participant_code',
        ),
        migrations.RenameField(
            model_name='participant',
            old_name='soil_rubble_yes',
            new_name='soil_rubble_description',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='commercial_compost',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='commercial_fertiliser',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='commercial_pesticide',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='compost',
        ),
        migrations.AddField(
            model_name='participant',
            name='compost_frequency',
            field=models.CharField(choices=[('3+ times', '3+ times in the last year'), ('1-3 times', '1-3 times in the last year'), ('Occasionally', 'Occasionally in the last 5 years'), ('Never', 'Not in the last 5 years/never')], default='3+ times', max_length=20),
        ),
        migrations.AddField(
            model_name='participant',
            name='compost_use',
            field=models.CharField(choices=[('Kitchen', 'I do compost kitchen waste'), ('Garden', 'I do compost garden waste'), ('Both', 'I do compost both kitchen and garden waste'), ('None', 'I do NOT compost any kitchen or garden waste')], default='Kitchen', max_length=20),
        ),
        migrations.AddField(
            model_name='participant',
            name='fertiliser_frequency',
            field=models.CharField(choices=[('3+ times', '3+ times in the last year'), ('1-3 times', '1-3 times in the last year'), ('Occasionally', 'Occasionally in the last 5 years'), ('Never', 'Not in the last 5 years/never')], default='3+ times', max_length=20),
        ),
        migrations.AddField(
            model_name='participant',
            name='veg_pesticide',
            field=models.CharField(choices=[('3+ times', '3+ times in the last year'), ('1-3 times', '1-3 times in the last year'), ('Occasionally', 'Occasionally in the last 5 years'), ('Never', 'Not in the last 5 years/never')], default='3+ times', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='area_for_growing_veg',
            field=models.CharField(choices=[('<1 sq m', '<1 square meter'), ('1-2 sq m', '1-2 square meters'), ('2-5 sq m', '2-5 square meters'), ('5-10 sq m', '5-10 square meters'), ('>10 sq m', '>10 square meters')], default='<1 sq m', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='average_gardening_hours',
            field=models.CharField(choices=[('0-1 hrs', '0-1 hours'), ('1-2 hrs', '1-2 hours'), ('2-5 hrs', '2-5 hours'), ('5-10 hrs', '5-10 hours'), ('>10 hrs', '>10 hours')], default='0-1 hrs', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='bird_feeders',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10),
        ),
        migrations.AlterField(
            model_name='participant',
            name='bumblebee',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='butterfly',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='construction_material',
            field=models.CharField(choices=[('Bricks', 'Bricks/stone walls'), ('Timber', 'Timber-framed walls'), ('Other', 'Other')], default='Bricks', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='domestic_cat',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='frog',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='goldfinch',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='hedgehog',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='house_rat',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='house_sparrow',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='ladybird',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='lawn_garden_area',
            field=models.CharField(choices=[('<10%', '<10%'), ('10-20%', '10-20%'), ('20-50%', '20-50%'), ('50-70%', '50-70%'), ('70-100%', '70-100%')], default='<10%', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='lawn_type',
            field=models.CharField(choices=[('Natural', 'Natural'), ('Artificial', 'Artificial')], default='Natural', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='mole',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='natural_garden_area',
            field=models.CharField(choices=[('<10%', '<10%'), ('10-20%', '10-20%'), ('20-50%', '20-50%'), ('50-70%', '50-70%'), ('70-100%', '70-100%')], default='<10%', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='ornamental_plant_fertiliser',
            field=models.CharField(choices=[('3+ times', '3+ times in the last year'), ('1-3 times', '1-3 times in the last year'), ('Occasionally', 'Occasionally in the last 5 years'), ('Never', 'Not in the last 5 years/never')], default='3+ times', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='ornamental_plant_garden_area',
            field=models.CharField(choices=[('<10%', '<10%'), ('10-20%', '10-20%'), ('20-50%', '20-50%'), ('50-70%', '50-70%'), ('70-100%', '70-100%')], default='<10%', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='ornamental_plant_pesticide',
            field=models.CharField(choices=[('3+ times', '3+ times in the last year'), ('1-3 times', '1-3 times in the last year'), ('Occasionally', 'Occasionally in the last 5 years'), ('Never', 'Not in the last 5 years/never')], default='3+ times', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='pond',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10),
        ),
        migrations.AlterField(
            model_name='participant',
            name='property_type',
            field=models.CharField(choices=[('Detached', 'Detached'), ('Semidetached', 'Semidetached'), ('Terraced', 'Terraced house'), ('Apartment', 'Apartment'), ('Other', 'Other')], default='Detached', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='purpose_of_garden',
            field=models.CharField(choices=[('Veg', 'Fruit and vegetable production'), ('Plants', 'Gardening of ornamental plants'), ('Natural Recreation', 'Recreational activity benefiting from natural environment'), ('Nonnatural Recreation', 'Recreational activity without any relevance of natural environment'), ('Storage', 'Storage space'), ('None', 'No specific use and limited leisure time spent in garden')], default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='participant',
            name='raised_beds',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10),
        ),
        migrations.AlterField(
            model_name='participant',
            name='red_fox',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='robin',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='sealed_garden_area',
            field=models.CharField(choices=[('<10%', '<10%'), ('10-20%', '10-20%'), ('20-50%', '20-50%'), ('50-70%', '50-70%'), ('70-100%', '70-100%')], default='<10%', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='slow_worm',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='soil_rubble',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10),
        ),
        migrations.AlterField(
            model_name='participant',
            name='total_garden_area',
            field=models.CharField(choices=[('<10 sq m', '<10 square meters'), ('10-100 sq m', '10-100 square meters'), ('100-200 sq m', '100-200 square meters'), ('200-500 sq m', '200-500 square meters'), ('>500 sq m', '>500 square meters')], default='<10 sq m', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='veg_garden_area',
            field=models.CharField(choices=[('<10%', '<10%'), ('10-20%', '10-20%'), ('20-50%', '20-50%'), ('50-70%', '50-70%'), ('70-100%', '70-100%')], default='<10%', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='veg_species',
            field=models.CharField(choices=[('Lettuce', 'Lettuce'), ('Spinach', 'Spinach'), ('Herbs', 'Herbs'), ('Carrots', 'Carrots'), ('Potatoes', 'Potatoes'), ('Onions', 'Onions'), ('Beans', 'Beans'), ('Tomatoes', 'Tomatoes'), ('Apples', 'Apples'), ('Pears', 'Pears'), ('Cherries', 'Cherries'), ('Strawberries', 'Strawberries'), ('Other', 'Other')], default='Lettuce', max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='wren',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Seasonally', 'Seasonally'), ('Yearly', 'Yearly'), ('Never', 'Never'), ('Unknown', 'Unknown')], default='Daily', max_length=20),
        ),
    ]