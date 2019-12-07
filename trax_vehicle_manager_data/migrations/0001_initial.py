# Generated by Django 2.2.5 on 2019-12-07 06:16

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cleaner_Id', models.CharField(blank=True, max_length=900)),
                ('cleaner_Name', models.CharField(blank=True, max_length=900)),
                ('cleaner_Age', models.CharField(blank=True, max_length=900)),
                ('cleaner_License_Number', models.CharField(blank=True, max_length=900)),
                ('cleaner_Address', models.CharField(blank=True, max_length=900)),
                ('cleaner_Contact_Number', models.CharField(blank=True, max_length=900)),
                ('cleaner_Salary', models.CharField(blank=True, max_length=900)),
                ('cleaner_joining_date', models.DateTimeField(blank=True)),
                ('cleaner_aadhar_number', models.CharField(blank=True, max_length=900)),
                ('cleaner_pan_number', models.CharField(blank=True, max_length=900)),
                ('cleaner_alternate_contact_number', models.CharField(blank=True, max_length=900)),
                ('cleaner_address_proof', models.CharField(blank=True, max_length=900)),
                ('cleaner_photo_id_proof', models.CharField(blank=True, max_length=900)),
            ],
            options={
                'verbose_name': 'Cleaner',
                'verbose_name_plural': 'Cleaners Master List',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('client_address', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_reference_no', models.IntegerField()),
                ('driver_driver_name', models.CharField(default='', max_length=264)),
                ('driver_vehicle_short_number', models.CharField(blank=True, max_length=12)),
                ('driver_vehicle_number', models.CharField(blank=True, max_length=12)),
                ('driver_vehicle_type', models.CharField(blank=True, max_length=264)),
                ('vehicle_type_of_module', models.CharField(blank=True, max_length=264)),
                ('driver_joining_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('driver_license_number', models.CharField(blank=True, max_length=264)),
                ('driver_aadhar_number', models.CharField(blank=True, default='', max_length=264)),
                ('driver_contact_number', models.CharField(blank=True, default='', max_length=264)),
                ('driver_pan_number', models.CharField(blank=True, default='', max_length=264)),
                ('driver_address_proof', models.CharField(blank=True, default='', max_length=264)),
                ('driver_photoid_proof', models.CharField(blank=True, default='', max_length=264)),
                ('driver_driver_bank_name', models.CharField(default='', max_length=264)),
                ('driver_bank_name', models.CharField(blank=True, default='', max_length=264)),
                ('driver_bank_account_number', models.CharField(blank=True, max_length=264)),
                ('driver_ban_ifsc_code', models.CharField(blank=True, default='', max_length=264)),
                ('driver_bank_branch', models.CharField(blank=True, default='', max_length=264)),
                ('driver_alternate_contact_number', models.CharField(blank=True, default='', max_length=264)),
                ('driver_license_residence_address', models.CharField(blank=True, default='', max_length=264)),
                ('driver_aadhar_card_residence_address', models.CharField(blank=True, default='', max_length=264)),
                ('driver_years_of_experience', models.CharField(blank=True, default='', max_length=264)),
                ('driver_last_employer_name', models.CharField(blank=True, default='', max_length=264)),
                ('driver_years_with_kruze_or_aaron', models.CharField(blank=True, default='', max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_name', models.CharField(blank=True, max_length=900)),
                ('expense_id', models.CharField(blank=True, max_length=900)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(blank=True, max_length=900)),
                ('vehicle_detail', models.CharField(blank=True, max_length=900)),
                ('bill_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('vehicle_type', models.CharField(blank=True, max_length=900)),
                ('chalak_malal', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=900)),
                ('company_name', models.CharField(blank=True, max_length=900)),
                ('odometer_reading', models.FloatField(blank=True)),
                ('bill_number', models.CharField(blank=True, max_length=900)),
                ('dealer_part_number', models.CharField(blank=True, max_length=900)),
                ('maintenance_dealer_name', models.CharField(blank=True, max_length=900)),
                ('particular', models.CharField(blank=True, max_length=900)),
                ('particular_details', models.CharField(blank=True, max_length=900)),
                ('quantity', models.FloatField(blank=True)),
                ('rate', models.FloatField(blank=True)),
                ('amount', models.FloatField(blank=True)),
                ('discount', models.FloatField(blank=True)),
                ('tax', models.FloatField(blank=True)),
                ('tds', models.FloatField(blank=True)),
                ('labour_charge', models.FloatField(blank=True)),
                ('total_amount', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diesel',
            fields=[
                ('expenses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trax_vehicle_manager_data.Expenses')),
                ('terminal_id', models.CharField(blank=True, max_length=900)),
                ('transaction_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('merchant', models.CharField(blank=True, max_length=900)),
                ('account_number', models.CharField(blank=True, max_length=900)),
                ('card_used', models.CharField(blank=True, max_length=900)),
                ('vehicle_number', models.CharField(blank=True, max_length=900)),
                ('vehicle_detail', models.CharField(blank=True, max_length=900)),
                ('transaction_type', models.CharField(blank=True, max_length=900)),
                ('diesel_rate', models.CharField(blank=True, max_length=900)),
                ('volume', models.CharField(blank=True, max_length=900)),
                ('amount_Rs', models.CharField(blank=True, max_length=900)),
                ('diesel_debit', models.CharField(blank=True, max_length=900)),
                ('diesel_credit', models.CharField(blank=True, max_length=900)),
                ('balance_Rs', models.CharField(blank=True, max_length=900)),
                ('odometer_reading', models.CharField(blank=True, max_length=900)),
                ('ownership', models.CharField(blank=True, max_length=900)),
            ],
            bases=('trax_vehicle_manager_data.expenses',),
        ),
        migrations.CreateModel(
            name='GarageBilling',
            fields=[
                ('maintenance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trax_vehicle_manager_data.Maintenance')),
            ],
            bases=('trax_vehicle_manager_data.maintenance',),
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('maintenance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trax_vehicle_manager_data.Maintenance')),
            ],
            bases=('trax_vehicle_manager_data.maintenance',),
        ),
        migrations.CreateModel(
            name='PoliceSettlements',
            fields=[
                ('maintenance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trax_vehicle_manager_data.Maintenance')),
            ],
            bases=('trax_vehicle_manager_data.maintenance',),
        ),
        migrations.CreateModel(
            name='RecurringExpenses',
            fields=[
                ('expenses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trax_vehicle_manager_data.Expenses')),
            ],
            bases=('trax_vehicle_manager_data.expenses',),
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_ownership_name', models.CharField(choices=[('ATPL', 'ATPL'), ('AT', 'AT'), ('CT', 'CT')], default='AT', max_length=900)),
                ('vehicle_id', models.CharField(blank=True, max_length=900)),
                ('vehicle_number', models.CharField(blank=True, max_length=900)),
                ('vehicle_card_number', models.CharField(blank=True, max_length=900)),
                ('vehicle_seating_capacity', models.CharField(blank=True, max_length=900)),
                ('minimum_average', models.CharField(blank=True, max_length=900)),
                ('incremental_average', models.CharField(blank=True, max_length=900)),
                ('vehicle_current_status', models.CharField(blank=True, max_length=900)),
                ('vehicle_buying_date', models.DateTimeField(blank=True)),
                ('vehicle_type', models.CharField(blank=True, max_length=900)),
                ('vehicle_ownership', models.CharField(blank=True, max_length=900)),
                ('vehicle_ownership_details', models.CharField(blank=True, max_length=900)),
                ('vehicle_manufacturer', models.CharField(blank=True, max_length=900)),
                ('vehicle_registered_number', models.CharField(blank=True, max_length=900)),
                ('cleaner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trax_vehicle_manager_data.Cleaners')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trax_vehicle_manager_data.Drivers')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles Master List',
            },
        ),
        migrations.AddField(
            model_name='maintenance',
            name='maintenance_vehicle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trax_vehicle_manager_data.Vehicles'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='expense_vehicle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trax_vehicle_manager_data.Vehicles'),
        ),
        migrations.CreateModel(
            name='Drivers_Odometer_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drivers_odometer_data_date_of_entry', models.DateTimeField(default=django.utils.timezone.now)),
                ('drivers_odometer_data_mobile_number', models.CharField(blank=True, max_length=12)),
                ('drivers_odometer_data_odometer_kilometer', models.CharField(blank=True, max_length=12)),
                ('drivers_odometer_data_cleaner_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trax_vehicle_manager_data.Cleaners')),
                ('drivers_odometer_data_driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trax_vehicle_manager_data.Drivers')),
                ('drivers_odometer_data_vehicle_number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trax_vehicle_manager_data.Vehicles')),
            ],
            options={
                'verbose_name': "Driver's Odometer",
                'verbose_name_plural': 'Drivers Odometer List',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_role', models.PositiveSmallIntegerField(choices=[(3, 'Office Team'), (2, 'Boss'), (1, 'System administrator')], default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='OilChange',
            fields=[
                ('recurringexpenses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trax_vehicle_manager_data.RecurringExpenses')),
            ],
            bases=('trax_vehicle_manager_data.recurringexpenses',),
        ),
        migrations.CreateModel(
            name='PUC',
            fields=[
                ('recurringexpenses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trax_vehicle_manager_data.RecurringExpenses')),
            ],
            bases=('trax_vehicle_manager_data.recurringexpenses',),
        ),
    ]
