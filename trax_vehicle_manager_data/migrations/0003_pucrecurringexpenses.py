# Generated by Django 2.2.5 on 2019-12-07 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trax_vehicle_manager_data', '0002_recurringexpensesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PUCRecurringExpenses',
            fields=[
                ('recurringexpensesmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trax_vehicle_manager_data.RecurringExpensesModel')),
                ('puc_number', models.CharField(blank=True, max_length=900)),
                ('center_name', models.CharField(blank=True, max_length=900)),
                ('test_date', models.DateTimeField(blank=True)),
                ('expiry_date', models.DateTimeField(blank=True)),
                ('puc_amount', models.CharField(blank=True, max_length=900)),
            ],
            bases=('trax_vehicle_manager_data.recurringexpensesmodel',),
        ),
    ]
