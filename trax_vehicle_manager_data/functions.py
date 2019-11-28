from trax_vehicle_manager_data.models import Drivers,Vehicles,Cleaners,Drivers_Odometer_Data,Expenses,Maintenance,Diesel

def diesel_volume_sum(list):
    sum = 0
    for diesel in list:
        sum = sum + int(diesel)
    return sum
