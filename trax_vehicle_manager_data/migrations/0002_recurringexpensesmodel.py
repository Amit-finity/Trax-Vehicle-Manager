# Generated by Django 2.2.5 on 2019-12-07 07:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trax_vehicle_manager_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecurringExpensesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_entry', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('current_odometer_km', models.CharField(blank=True, max_length=900)),
                ('last_odometer_km', models.CharField(blank=True, max_length=900)),
                ('current_km_date', models.DateTimeField(blank=True)),
                ('recurring_expense_vehicle_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='trax_vehicle_manager_data.Vehicles')),
            ],
        ),
    ]
