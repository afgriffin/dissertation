from django.test import TestCase, Client
from django.urls import reverse
from .models import Participant

# Create your tests here.
class ParticipantTests(TestCase):

    def setUp(self):
        self.participant = Participant.objects.create(
            name = 'John Smith',
            preferred_name = 'John',
            email = 'john@email.com',
            contact_preference = True,
            address = 'Singleton Park, Sketty, Swansea SA2 8PP',
            year_property_built = '1950',
            property_type = 'Terraced',
            property_type_other = 'end of terrace',
            construction_material = 'Timber',
            construction_material_other = 'wood',
            number_of_people = 5,
            purpose_of_garden = 'Storage',
            area_for_growing_veg = '5-10 sq m',
            average_gardening_hours = '>10 hrs',
            total_garden_area = '10-100 sq m',
            sealed_garden_area = '10-20%',
            lawn_garden_area = '50-70%',
            lawn_type = 'Artificial',
            veg_garden_area = '20-50%',
            ornamental_plant_garden_area = '<10%',
            natural_garden_area = '70-100%',
            veg_species = 'Herbs',
            veg_species_other = 'Peaches',
            raised_beds = 'No',
            compost_use = 'Both',
            compost_frequency = '1-3 times',
            fertiliser_frequency = 'Occasionally',
            latest_compost_purchase = 'Last week',
            veg_pesticide = '3+ times',
            ornamental_plant_fertiliser = 'Never',
            ornamental_plant_pesticide = '1-3 times',
            soil_rubble = 'No',
            soil_rubble_description = 'Pieces of brick',
            bird_feeders = 'Yes',
            pond = 'No',
            house_sparrow = 'Unknown',
            goldfinch = 'Never',
            robin = 'Yearly',
            wren = 'Seasonally',
            domestic_cat = 'Monthly',
            red_fox = 'Weekly',
            hedgehog = 'Daily',
            slow_worm = 'Unknown',
            frog = 'Never',
            mole = 'Yearly',
            house_rat = 'Seasonally',
            bumblebee = 'Monthly',
            ladybird = 'Weekly',
            butterfly = 'Daily',
            other_notable_wildlife = 'turtles seasonally',
            sample_1_description = 'back garden',
            sample_2_description = 'left side garden',
            sample_3_description = 'right side garden',
            sample_4_description = 'front garden',
            sample_5_description = 'vegetable patch',
            agreement = True
        )
    
    def test_participant_listing(self):
        self.assertEqual(f'{self.participant.name}', 'John Smith'),
        self.assertEqual(f'{self.participant.preferred_name}', 'John'),
        self.assertEqual(f'{self.participant.email}', 'john@email.com'),
        self.assertEqual(f'{self.participant.contact_preference}', 'True'),
        self.assertEqual(f'{self.participant.address}', 'Singleton Park, Sketty, Swansea SA2 8PP'),
        self.assertEqual(f'{self.participant.year_property_built}', '1950'),
        self.assertEqual(f'{self.participant.property_type}', 'Terraced'),
        self.assertEqual(f'{self.participant.property_type_other}', 'end of terrace'),
        self.assertEqual(f'{self.participant.construction_material}', 'Timber'),
        self.assertEqual(f'{self.participant.construction_material_other}', 'wood'),
        self.assertEqual(f'{self.participant.number_of_people}', '5'),
        self.assertEqual(f'{self.participant.purpose_of_garden}', 'Storage'),
        self.assertEqual(f'{self.participant.area_for_growing_veg}', '5-10 sq m'),
        self.assertEqual(f'{self.participant.average_gardening_hours}', '>10 hrs'),
        self.assertEqual(f'{self.participant.total_garden_area}', '10-100 sq m'),
        self.assertEqual(f'{self.participant.sealed_garden_area}', '10-20%'),
        self.assertEqual(f'{self.participant.lawn_garden_area}','50-70%'),
        self.assertEqual(f'{self.participant.lawn_type}', 'Artificial'),
        self.assertEqual(f'{self.participant.veg_garden_area}', '20-50%'),
        self.assertEqual(f'{self.participant.ornamental_plant_garden_area}', '<10%'),
        self.assertEqual(f'{self.participant.natural_garden_area}', '70-100%'),
        self.assertEqual(f'{self.participant.veg_species}', 'Herbs'),
        self.assertEqual(f'{self.participant.veg_species_other}', 'Peaches'),
        self.assertEqual(f'{self.participant.raised_beds}', 'No'),
        self.assertEqual(f'{self.participant.compost_use}', 'Both'),
        self.assertEqual(f'{self.participant.compost_frequency}', '1-3 times'),
        self.assertEqual(f'{self.participant.fertiliser_frequency}', 'Occasionally'),
        self.assertEqual(f'{self.participant.latest_compost_purchase}', 'Last week'),
        self.assertEqual(f'{self.participant.veg_pesticide}','3+ times'),
        self.assertEqual(f'{self.participant.ornamental_plant_fertiliser}', 'Never'),
        self.assertEqual(f'{self.participant.ornamental_plant_pesticide}', '1-3 times'),
        self.assertEqual(f'{self.participant.soil_rubble}', 'No'),
        self.assertEqual(f'{self.participant.soil_rubble_description}', 'Pieces of brick'),
        self.assertEqual(f'{self.participant.bird_feeders}', 'Yes'),
        self.assertEqual(f'{self.participant.pond}', 'No'),
        self.assertEqual(f'{self.participant.house_sparrow}', 'Unknown'),
        self.assertEqual(f'{self.participant.goldfinch}', 'Never'),
        self.assertEqual(f'{self.participant.robin}', 'Yearly'),
        self.assertEqual(f'{self.participant.wren}', 'Seasonally'),
        self.assertEqual(f'{self.participant.domestic_cat}', 'Monthly'),
        self.assertEqual(f'{self.participant.red_fox}', 'Weekly'),
        self.assertEqual(f'{self.participant.hedgehog}', 'Daily'),
        self.assertEqual(f'{self.participant.slow_worm}', 'Unknown'),
        self.assertEqual(f'{self.participant.frog}', 'Never'),
        self.assertEqual(f'{self.participant.mole}', 'Yearly'),
        self.assertEqual(f'{self.participant.house_rat}', 'Seasonally'),
        self.assertEqual(f'{self.participant.bumblebee}', 'Monthly'),
        self.assertEqual(f'{self.participant.ladybird}', 'Weekly'),
        self.assertEqual(f'{self.participant.butterfly}', 'Daily'),
        self.assertEqual(f'{self.participant.other_notable_wildlife}', 'turtles seasonally'),
        self.assertEqual(f'{self.participant.sample_1_description}', 'back garden'),
        self.assertEqual(f'{self.participant.sample_2_description}', 'left side garden'),
        self.assertEqual(f'{self.participant.sample_3_description}', 'right side garden'),
        self.assertEqual(f'{self.participant.sample_4_description}', 'front garden'),
        self.assertEqual(f'{self.participant.sample_5_description}', 'vegetable patch'),
        self.assertEqual(f'{self.participant.agreement}', 'True')
