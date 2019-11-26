from django import forms
from trax_vehicle_manager_data.models import CustomUser,Drivers,Cleaners,Vehicles,Expenses,Diesel,Maintenance,GarageBilling,Insurance,PoliceSettlements,RecurringExpenses,PUC,OilChange,Client,Drivers_Odometer_Data
from bootstrap_modal_forms.forms import BSModalForm

class MaintenanceForm(BSModalForm):
    class Meta:
        model = Maintenance
        fields = ('expense_name',
        'expense_id',
        'vehicle_number',
        'vehicle_detail',
        'vehicle_type',
        'chalak_malal',
        'company_name',
        'odometer_reading',
        'bill_number',
        'dealer_part_number',
        'maintenance_dealer_name',
        'particular',
        'particular_details',
        'quantity',
        'rate',
        'amount',
        'discount',
        'tax',
        'tds',
        'labour_charge',
        'total_amount')  

class DriverForm(BSModalForm):
    class Meta:
        model = Drivers
        fields = ('driver_reference_no',
        'driver_driver_name',
        'driver_vehicle_short_number',
        'driver_vehicle_number',
        'driver_vehicle_type',
        'vehicle_type_of_module',
        'driver_license_number',
        'driver_aadhar_number',
        'driver_contact_number',
        'driver_pan_number',
        'driver_address_proof',
        'driver_photoid_proof',
        'driver_driver_bank_name',
        'driver_bank_name',
        'driver_bank_account_number',
        'driver_ban_ifsc_code',
        'driver_bank_branch',
        'driver_alternate_contact_number',
        'driver_license_residence_address',
        'driver_aadhar_card_residence_address',
        'driver_years_of_experience',
        'driver_last_employer_name',
        'driver_years_with_kruze_or_aaron')

class DriverOdometerForm(BSModalForm):
    class Meta:
        model = Drivers_Odometer_Data
        fields = ('drivers_odometer_data_driver_id',
        'drivers_odometer_data_mobile_number',
        'drivers_odometer_data_vehicle_number',
        'drivers_odometer_data_odometer_kilometer',
        'drivers_odometer_data_cleaner_id')

class DieselOdometerReadingUpdateForm(BSModalForm):
    class Meta:
        model = Diesel
        fields = ('odometer_reading',)

class DieselDataForm(BSModalForm):
    class Meta:
        model = Diesel
        fields = ('expense_name',
        'expense_id',
        'expense_vehicle_id',
        'terminal_id',
        'transaction_date',
        'merchant',
        'account_number',
        'card_used',
        'vehicle_number',
        'vehicle_detail',
        'transaction_type',
        'diesel_rate',
        'volume',
        'amount_Rs',
        'balance_Rs',
        'odometer_reading',
        'ownership')

