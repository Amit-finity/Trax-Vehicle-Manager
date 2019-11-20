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

