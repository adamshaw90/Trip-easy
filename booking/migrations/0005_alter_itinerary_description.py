# Generated by Django 4.2.17 on 2024-12-10 07:47

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_itinerary_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Description'),
        ),
    ]
