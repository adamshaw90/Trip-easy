# Generated by Django 4.2.17 on 2024-12-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_itinerary_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='itineraries/'),
        ),
    ]
