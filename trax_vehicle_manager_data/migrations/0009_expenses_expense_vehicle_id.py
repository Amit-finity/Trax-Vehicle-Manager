# Generated by Django 2.2.5 on 2019-11-20 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trax_vehicle_manager_data', '0008_auto_20191120_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='expense_vehicle_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trax_vehicle_manager_data.Vehicles'),
            preserve_default=False,
        ),
    ]
