from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from trax_vehicle_manager_data.models import CustomUser,Drivers,Cleaners,Vehicles,Expenses,Diesel,Maintenance,GarageBilling,Insurance,PoliceSettlements,RecurringExpenses,PUC,OilChange,Client,Drivers_Odometer_Data,RecurringExpensesModel,PUCRecurringExpenses,OilChangeRecurringExpenses,HubGreasingRecurringExpenses

# Register your models here.
class DriversAdmin(ImportExportModelAdmin):
    search_fields = ["driver_driver_name", "driver_contact_number","driver_vehicle_number"]
    list_filter = ["driver_vehicle_short_number", "driver_contact_number"]
    list_display = [
        "pk",
        "driver_driver_name",
        "driver_vehicle_short_number",
        "driver_license_number",
        "driver_aadhar_number",
        "driver_contact_number",
        ]
    pass

class VehiclesAdmin(ImportExportModelAdmin):
    list_display = [
        "pk",
        "vehicle_id",
        "vehicle_number",
        "vehicle_card_number",
        "vehicle_seating_capacity",
        "minimum_average",
        "incremental_average",
        "vehicle_current_status",
        "vehicle_buying_date",
        "vehicle_type",
        "vehicle_ownership",
        "vehicle_ownership_details",
        "vehicle_manufacturer",
        "vehicle_registered_number"
    ]

class CleanersAdmin(ImportExportModelAdmin):
    list_display = [
        "pk",
        "cleaner_Id",
        "cleaner_Name",
        "cleaner_Age",
        "cleaner_License_Number",
        "cleaner_Address",
        "cleaner_Contact_Number",
        "cleaner_Salary"
    ]




admin.site.register(CustomUser)
admin.site.register(Drivers,DriversAdmin)
admin.site.register(Cleaners,CleanersAdmin)
admin.site.register(Vehicles,VehiclesAdmin)
admin.site.register(Expenses)
admin.site.register(Diesel)
admin.site.register(Maintenance)
admin.site.register(GarageBilling)
admin.site.register(Insurance)
admin.site.register(PoliceSettlements)
admin.site.register(RecurringExpenses)
admin.site.register(PUC)
admin.site.register(OilChange)
admin.site.register(Client)
admin.site.register(Drivers_Odometer_Data)
admin.site.register(RecurringExpensesModel)
admin.site.register(PUCRecurringExpenses)
admin.site.register(OilChangeRecurringExpenses)
admin.site.register(HubGreasingRecurringExpenses)