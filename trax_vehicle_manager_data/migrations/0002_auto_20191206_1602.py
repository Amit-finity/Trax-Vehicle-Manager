# Generated by Django 2.2.5 on 2019-12-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trax_vehicle_manager_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diesel',
            name='diesel_credit',
            field=models.CharField(blank=True, max_length=900),
        ),
        migrations.AddField(
            model_name='diesel',
            name='diesel_debit',
            field=models.CharField(blank=True, max_length=900),
        ),
    ]
