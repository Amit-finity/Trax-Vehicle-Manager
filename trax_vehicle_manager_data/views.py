from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)


from trax_vehicle_manager_data.models import Drivers,Vehicles,Cleaners,Drivers_Odometer_Data,Expenses,Maintenance,Diesel,CustomUser,RecurringExpensesModel,PUCRecurringExpenses,OilChangeRecurringExpenses,HubGreasingRecurringExpenses
from trax_vehicle_manager_data.forms import MaintenanceForm,DriverForm,DriverOdometerForm,DieselOdometerReadingUpdateForm,DieselDataForm,DriverKYCForm,VehicleDataForm,PUCDataForm,OilChangeForm,HubGreasingForm

from trax_vehicle_manager_data import functions


from tablib import Dataset

from django.db.models import Sum
from math import ceil
from django.db.models import FloatField
from django.db.models.functions import Cast
# Create your views here.
#<----------------- Authentication Views --------------------

#Login Page view
def user_login(request):
    """Logs in a user if the credentials are valid and the user is active,
    else redirects to the same page and displays an error message."""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('trax_vehicle_manager_data:vehicles'))
        else:
            return render(request, 'trax_vehicle_manager_data/registration/login.html',{'error_message': 'Username or Password Incorrect!'})

    else:
        return render(request, 'trax_vehicle_manager_data/registration/login.html')

#Register Page view
def user_sign_up(request):
    """Registers a user"""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'trax_vehicle_manager_data/registration/register.html',{'error_message':'Passwords do not match!'})
        if CustomUser.objects.filter(username = username).exists():
            return render(request, 'trax_vehicle_manager_data/registration/register.html',{'error_message':'Username already exists!'})
        else:
            # Role 2 is for admin, 1 is for super admin.
            user = CustomUser.objects.create(username=username, password= make_password(password), user_role=2)
            login(request, user)
            return HttpResponseRedirect(reverse('trax_vehicle_manager_data:vehicles'))
    else:
        return render(request, 'trax_vehicle_manager_data/registration/register.html')

# Logout
def user_sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('trax_vehicle_manager_data:login'))

#forget password view
def forgetpassword(request):
    return render(request,'trax_vehicle_manager_data/forget_password.html')

#</----------------- Authentication Views --------------------


#<----------------- Projects Pages  Views --------------------



def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'trax_vehicle_manager_data/maintenance_data.html')

def fileimport(request):
    return render(request,'trax_vehicle_manager_data/import.html')

def maintenance_company_show_report(request):
    return render(request,'trax_vehicle_manager_data/maintenance_company_show_report.html')

#Vehicle page view
@login_required(login_url='/login')
def vehicles(request):
    vehicleobjectlist = []
    if request.method == "POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        vehicleobjectlist = Vehicles.objects.filter(vehicle_buying_date__range=[date1,date2]).all()
        filter_date = "True"
        data = {'vehicleobjectlist':vehicleobjectlist,'date1':date1,'date2':date2,'filter_date':filter_date}
    else:
        vehicleobjectlist = Vehicles.objects.all()
        data = {'vehicleobjectlist':vehicleobjectlist}
    return render(request,'trax_vehicle_manager_data/vehicles.html',data)

#Driver master page view
@login_required(login_url='/login')
def driver_master(request):
    driver_master_objects = Drivers.objects.all()
    data = {'driver_master_list':driver_master_objects}
    return render(request,'trax_vehicle_manager_data/driver_master.html',data)

#Driver Odometer view
@login_required(login_url='/login')
def driver_odometer(request):
    driver_odometer_objects = Drivers_Odometer_Data.objects.all()
    data = {'driver_odometer_list': driver_odometer_objects}
    return render(request,'trax_vehicle_manager_data/driver_odometer.html',data)

#Driver Usage page view
@login_required(login_url='/login')
def drivers_usage(request):
    driver_objects = Drivers.objects.all()
    latest_average_dict = {}
    latest_date_of_average_dict = {}
    for one_driver_object in driver_objects:
        driver_odometer_objects=Drivers_Odometer_Data.objects.filter(drivers_odometer_data_driver_id=Drivers.objects.get(pk=one_driver_object.pk)).all()
        count_driver_odometer_objects=Drivers_Odometer_Data.objects.filter(drivers_odometer_data_driver_id=Drivers.objects.get(pk=one_driver_object.pk)).all().count()
        if count_driver_odometer_objects == 0:
            latest_date_of_average_dict[one_driver_object.pk]="None"
        else:
            latest_driver_odometer_object = driver_odometer_objects.latest('drivers_odometer_data_date_of_entry')
            latest_date_of_average_dict[one_driver_object.pk]=latest_driver_odometer_object.drivers_odometer_data_date_of_entry
    for one_driver_object in driver_objects:
        driver_odometer_filered_based_on_driver_pk = Drivers_Odometer_Data.objects.filter(drivers_odometer_data_driver_id=Drivers.objects.get(pk=one_driver_object.pk)).all()
        count_driver_odometer_filered_based_on_driver_pk = Drivers_Odometer_Data.objects.filter(drivers_odometer_data_driver_id=Drivers.objects.get(pk=one_driver_object.pk)).all().count()
        if count_driver_odometer_filered_based_on_driver_pk == 0:
            latest_average_dict[one_driver_object.pk]="None"
        else:
            driver_odometer_filered_based_on_driver_pk = Drivers_Odometer_Data.objects.filter(drivers_odometer_data_driver_id=Drivers.objects.get(pk=one_driver_object.pk)).all()
            objects_odometer_list = []
            for driver_odometer_filered_based_on_driver_pk_single in driver_odometer_filered_based_on_driver_pk:
                objects_odometer_list.append(int(driver_odometer_filered_based_on_driver_pk_single.drivers_odometer_data_odometer_kilometer))
            objects_km_per_day = []
            for i in range(1,len(objects_odometer_list)):
                x = objects_odometer_list[i] - objects_odometer_list[i-1]
                objects_km_per_day.append(x)
            odometer_total = 0
            objects_average_list = []
            for j in range(0,len(objects_km_per_day)):
                odometer_total = (odometer_total+objects_km_per_day[j])
                average_total = odometer_total/(j+1)
                objects_average_list.append(average_total)
                latest_average_dict[one_driver_object.pk]=objects_average_list[-1]
    
    data = {'driver_objects':driver_objects,'latest_date_of_average_dict':latest_date_of_average_dict,'latest_average_dict':latest_average_dict}
    return render(request,'trax_vehicle_manager_data/driver_usage.html',data)

#Drivers Details Page View
@login_required(login_url='/login')
def drivers_details(request,pk):
    #Driver_odometer Objects
    driver_odometer_filered_based_on_driver_pk = Drivers_Odometer_Data.objects.filter(drivers_odometer_data_driver_id=Drivers.objects.get(pk=pk)).all()
    #Km and Average
    objects_odometer_list = []
    for driver_odometer_filered_based_on_driver_pk_single in driver_odometer_filered_based_on_driver_pk:
        objects_odometer_list.append(int(driver_odometer_filered_based_on_driver_pk_single.drivers_odometer_data_odometer_kilometer))
    objects_km_per_day = []
    for i in range(1,len(objects_odometer_list)):
        x = objects_odometer_list[i] - objects_odometer_list[i-1]
        objects_km_per_day.append(x)
    odometer_total = 0
    objects_average_list = []
    for j in range(0,len(objects_km_per_day)):
        odometer_total = (odometer_total+objects_km_per_day[j])
        average_total = odometer_total/(j+1)
        objects_average_list.append(average_total)
    objects_km_per_day.insert(0,0)
    objects_average_list.insert(0,0)
    driver_odometer_km_average_dict = {}
    counter = 0
    driver_odometer_filered_based_on_driver_pk_in_desc = Drivers_Odometer_Data.objects.filter(drivers_odometer_data_driver_id=Drivers.objects.get(pk=pk)).all().order_by('-pk')
    for driver_odometer_filered_based_on_driver_pk_desc in driver_odometer_filered_based_on_driver_pk_in_desc:
        counter = counter + 1
        driver_odometer_km_average_dict[driver_odometer_filered_based_on_driver_pk_desc]=[objects_km_per_day[len(objects_km_per_day)-counter],objects_average_list[len(objects_average_list)-counter]]
    driver_name = Drivers.objects.get(pk=pk).driver_driver_name
    driver_contact = Drivers.objects.get(pk=pk).driver_contact_number 
    data = {'driver_odometer_filered_based_on_driver_pk':driver_odometer_filered_based_on_driver_pk,'driver_odometer_km_average_dict':driver_odometer_km_average_dict,'driver_name':driver_name,'driver_contact':driver_contact}
    return render(request,'trax_vehicle_manager_data/driver_detail.html',data)

#Driver Odometer form page view
def drivers_odometer_form(request):
    Drivers_dict = Drivers.objects.all()
    vehicles_dict = Vehicles.objects.all()
    Cleaners_dict = Cleaners.objects.all()
    data = {'drivers':Drivers_dict,'vehicles':vehicles_dict,'cleaners':Cleaners_dict}
    return render(request,'trax_vehicle_manager_data/driver_form.html',data)

#Driver Odometer form submit page view
@login_required(login_url='/login')
def drivers_odometer_form_submit(request):
    if request.method == "POST":
        driverdata_driver_id = request.POST['driverdata_driver_id']
        driverdata_driver_mobile_number = request.POST['driverdata_driver_mobile_number']
        driverdata_vehicle_number = request.POST['driverdata_vehicle_number']
        driverdata_odometer = request.POST['driverdata_odometer']
        driverdata_cleaner_id = request.POST['driverdata_cleaner_id']
        DriversOdometerData=Drivers_Odometer_Data.objects.create(drivers_odometer_data_driver_id=Drivers.objects.get(pk=driverdata_driver_id),
                                                                   drivers_odometer_data_mobile_number=driverdata_driver_mobile_number,
                                                                   drivers_odometer_data_vehicle_number=Vehicles.objects.get(pk=driverdata_vehicle_number),
                                                                   drivers_odometer_data_odometer_kilometer=driverdata_odometer,
                                                                   drivers_odometer_data_cleaner_id=Cleaners.objects.get(pk=driverdata_cleaner_id),
        )
    #return render(request,'trax_vehicle_manager_data/driver_successfull_message.html')
    return HttpResponseRedirect(reverse('trax_vehicle_manager_data:drivers_odometer_successfull_form'))

#Driver odometer successfull form page view
@login_required(login_url='/login')
def drivers_odometer_successfull_form(request):
    return render(request,'trax_vehicle_manager_data/driver_successfull_message.html')

#Full diesel details page view
@login_required(login_url='/login')
def full_diesel_details(request):
    diesel_objects = Diesel.objects.all()
    data = {'diesel_objects':diesel_objects}
    return render(request,'trax_vehicle_manager_data/full_diesel_details.html',data)


@login_required(login_url='/login')
def full_diesel_details_filtered_by_date(request):
    dieselobjectlist = []
    if request.method == "POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        dieselobjectlist = Diesel.objects.filter(transaction_date__range=[date1,date2]).all()
        filter_date = "True"
        data =  {'dieselobjectlist':dieselobjectlist,'date1':date1,'date2':date2,'filter_date':filter_date}
    else:
        dieselobjectlist = Diesel.objects.all()
        data =  {'dieselobjectlist':dieselobjectlist}
    return render(request,'trax_vehicle_manager_data/full_diesel_detail_filtered_by_date.html',data)


#Vehicle Diesel Report view
@login_required(login_url='/login')
def vehicle_diesel_report(request):
    if request.method == "POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        vehicle_objects_all = Vehicles.objects.all()
        vehicle_diesel_litre = {}
        vehicle_amount_dict = {}
        vehicle_km_runs_dict = {}
        vehicle_average_dict = {}
        vehicle_performance_dict = {}
        for vehicle in vehicle_objects_all:
            vehicle_diesel_litre_value_list = []
            vehicle_diesel_amount_value_list = []
            vehicle_diesel_litre_value_list=Diesel.objects.filter(expense_vehicle_id=vehicle).values_list('volume',flat=True)
            vehicle_diesel_amount_value_list=Diesel.objects.filter(expense_vehicle_id=vehicle).values_list('amount_Rs',flat=True)
            vehicle_diesel_litre[vehicle.pk]=functions.diesel_volume_sum(vehicle_diesel_litre_value_list)
            vehicle_amount_dict[vehicle.pk]=functions.diesel_volume_sum(vehicle_diesel_amount_value_list)
            one_vehicle_amount_value=functions.diesel_volume_sum(vehicle_diesel_amount_value_list) 
            diesel_objects=Diesel.objects.filter(expense_vehicle_id=vehicle).all()
            diesel_objects_count=Diesel.objects.filter(expense_vehicle_id=vehicle).all().count()
            if diesel_objects_count>1:
                diesel_object_filtered_by_date=diesel_objects.filter(transaction_date__range=[date1,date2])
                latest_diesel_object=diesel_object_filtered_by_date.latest('transaction_date')
                earliest_diesel_object=diesel_object_filtered_by_date.earliest('transaction_date')
                km_runs=int(latest_diesel_object.odometer_reading)-int(earliest_diesel_object.odometer_reading)
                average=one_vehicle_amount_value/km_runs
                performance=average-float(vehicle.minimum_average)
                vehicle_km_runs_dict[vehicle.pk]=km_runs
                vehicle_average_dict[vehicle.pk]=average
                if performance>0:
                    vehicle_performance_dict[vehicle.pk]="Good"
                else:
                    vehicle_performance_dict[vehicle.pk]="Bad"
            else:
                vehicle_km_runs_dict[vehicle.pk]=0
                vehicle_average_dict[vehicle.pk]=0
                vehicle_performance_dict[vehicle.pk]="None"
        data={'vehicle_performance_dict':vehicle_performance_dict,'vehicle_average_dict':vehicle_average_dict,'vehicle_km_runs_dict':vehicle_km_runs_dict,'vehicle_objects_all':vehicle_objects_all,'vehicle_amount_dict':vehicle_amount_dict,'vehicle_diesel_litre':vehicle_diesel_litre}
    else:
        vehicle_objects_all = Vehicles.objects.all()
        vehicle_diesel_litre = {}
        vehicle_amount_dict = {}
        vehicle_km_runs_dict = {}
        vehicle_average_dict = {}
        vehicle_performance_dict = {}
        for vehicle in vehicle_objects_all:
            vehicle_diesel_litre_value_list = []
            vehicle_diesel_amount_value_list = []
            vehicle_diesel_litre_value_list=Diesel.objects.filter(expense_vehicle_id=vehicle).values_list('volume',flat=True)
            vehicle_diesel_amount_value_list=Diesel.objects.filter(expense_vehicle_id=vehicle).values_list('amount_Rs',flat=True)
            vehicle_diesel_litre[vehicle.pk]=functions.diesel_volume_sum(vehicle_diesel_litre_value_list)
            vehicle_amount_dict[vehicle.pk]=functions.diesel_volume_sum(vehicle_diesel_amount_value_list)
        data={'vehicle_performance_dict':vehicle_performance_dict,'vehicle_average_dict':vehicle_average_dict,'vehicle_km_runs_dict':vehicle_km_runs_dict,'vehicle_objects_all':vehicle_objects_all,'vehicle_amount_dict':vehicle_amount_dict,'vehicle_diesel_litre':vehicle_diesel_litre}  
    
    return render(request,'trax_vehicle_manager_data/vehicle_diesel_report.html',data)

@login_required(login_url='/login')
def vehicle_diesel_report_one_vehicle(request,pk):
    if request.method=="POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        diesel_objects = Diesel.objects.filter(expense_vehicle_id=pk).all() 
        diesel_objects_filter_by_transaction_date = diesel_objects.filter(transaction_date__range=[date1,date2]).all()
        total_liters = 0
        total_amount = 0
        total_odometer = 0
        for one_diesel_objects in diesel_objects_filter_by_transaction_date:
            total_liters=total_liters+int(one_diesel_objects.volume)
            total_amount=total_amount+int(one_diesel_objects.amount_Rs)
            total_odometer=total_odometer+int(one_diesel_objects.odometer_reading)
        vehicle_number = Vehicles.objects.get(pk=pk).vehicle_number
        pk = Vehicles.objects.get(pk=pk)
        filter_date = "True"
        data = {'pk':pk,'date1':date1,'date2':date2,'filter_date':filter_date,'diesel_objects':diesel_objects_filter_by_transaction_date,'total_liters':total_liters,'total_amount':total_amount,'total_odometer':total_odometer,'vehicle_number':vehicle_number}
    else:
        total_liters = 0
        total_amount = 0
        total_odometer = 0
        diesel_objects = Diesel.objects.filter(expense_vehicle_id=pk).all() 
        for one_diesel_objects in diesel_objects:
            total_liters=total_liters+int(one_diesel_objects.volume)
            total_amount=total_amount+int(one_diesel_objects.amount_Rs)
            total_odometer=total_odometer+int(one_diesel_objects.odometer_reading)
        vehicle_number = Vehicles.objects.get(pk=pk).vehicle_number
        pk = Vehicles.objects.get(pk=pk)
        data = {'pk':pk,'diesel_objects':diesel_objects,'total_liters':total_liters,'total_amount':total_amount,'total_odometer':total_odometer,'vehicle_number':vehicle_number}
    return render(request,'trax_vehicle_manager_data/view_vehicle_diesel_report.html',data)


#Diesel transaction details page view
@login_required(login_url='/login')
def diesel_transaction_details(request):
    return render(request,'trax_vehicle_manager_data/diesel_transaction_details.html')

#Diesel transaction tally page view
@login_required(login_url='/login')
def transaction_tally(request):
    if request.method=="POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        diesel_objects = Diesel.objects.filter(transaction_date__range=[date1,date2]).all()
        filter_date = "True"
        data = {'date1':date1,'date2':date2,'filter_date':filter_date,'diesel_objects':diesel_objects}
    else:
        diesel_objects = Diesel.objects.all()
        data = {'diesel_objects':diesel_objects}
    return render(request,'trax_vehicle_manager_data/diesel_transaction_tally.html',data)

#Diesel delete data page view
@login_required(login_url='/login')
def diesel_delete_data(request):
    return render(request,'trax_vehicle_manager_data/diesel_delete.html')

#Maintenance Data page view
@login_required(login_url='/login')
def maintenance_data(request):
    maintenanceobjectlist = []
    if request.method == "POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        maintenanceobjectlist = Maintenance.objects.filter(bill_date__range=[date1,date2]).all()
        filter_date = "True"
        data =  {'maintenance_data_objects':maintenanceobjectlist,'date1':date1,'date2':date2,'filter_date':filter_date}
    else:
        maintenanceobjectlist = Maintenance.objects.all()
        data = {'maintenance_data_objects':maintenanceobjectlist}
    return render(request,'trax_vehicle_manager_data/maintenance_data.html',data)

#Maintenance Details page view
@login_required(login_url='/login')
def maintenance_details(request):
    vehicleobjectlist = []
    if request.method == "POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        vehicleobjectlist = Vehicles.objects.all()
        filter_date = "True"
        vehicle_km_sum = {}
        vehicle_amount_sum = {}
        vehicle_objects_all = Vehicles.objects.all()
        vehicle_object_used_for_maintenance_form=Vehicles.objects.all()
        maintenance_objects_within_bill_date = Maintenance.objects.filter(bill_date__range=[date1,date2]).all()
        total_amount = 0
        for maintenance_data in maintenance_objects_within_bill_date:
            total_amount = total_amount + int(maintenance_data.amount)        
        for vehicle in vehicle_objects_all:
            vehicle_odometer_value_list = []
            vehicle_amount_value_list = []
            vehicle_odometer_value_list = Maintenance.objects.filter(maintenance_vehicle_id=vehicle).values_list('odometer_reading',flat=True)
            vehicle_odometer_value_list_within_bill_date = vehicle_odometer_value_list.filter(bill_date__range=[date1,date2]).all()
            vehicle_amount_value_list = Maintenance.objects.filter(maintenance_vehicle_id=vehicle).values_list('amount',flat=True)
            vehicle_amount_value_list_within_bill_date = vehicle_amount_value_list.filter(bill_date__range=[date1,date2]).all()
            vehicle_km_sum[vehicle.pk]=functions.diesel_volume_sum(vehicle_odometer_value_list_within_bill_date)
            vehicle_amount_sum[vehicle.pk]=functions.diesel_volume_sum(vehicle_amount_value_list_within_bill_date)
        data = {'vehicles':vehicle_object_used_for_maintenance_form,'total_amount':total_amount,'maintenance_objects':maintenance_objects_within_bill_date,'vehicle_km_sum':vehicle_km_sum,'vehicle_amount_sum':vehicle_amount_sum,'vehicleobjectlist':vehicleobjectlist,'date1':date1,'date2':date2,'filter_date':filter_date}
    else:
        vehicle_km_sum = {}
        vehicle_amount_sum = {}
        vehicle_objects_all = Vehicles.objects.all()
        maintenance_objects = Maintenance.objects.all()
        vehicle_object_used_for_maintenance_form=Vehicles.objects.all()
        total_amount = 0
        for maintenance_data in maintenance_objects:
            total_amount = total_amount + int(maintenance_data.amount)     
        for vehicle in vehicle_objects_all:
            vehicle_odometer_value_list = []
            vehicle_amount_value_list = []
            vehicle_odometer_value_list = Maintenance.objects.filter(maintenance_vehicle_id=vehicle).values_list('odometer_reading',flat=True)
            vehicle_amount_value_list = Maintenance.objects.filter(maintenance_vehicle_id=vehicle).values_list('amount',flat=True)
            vehicle_km_sum[vehicle.pk]=functions.diesel_volume_sum(vehicle_odometer_value_list)
            vehicle_amount_sum[vehicle.pk]=functions.diesel_volume_sum(vehicle_amount_value_list)
        data = {'vehicles':vehicle_object_used_for_maintenance_form,'total_amount':total_amount,'maintenance_objects':maintenance_objects,'vehicle_km_sum':vehicle_km_sum,'vehicle_amount_sum':vehicle_amount_sum,'vehicleobjectlist':vehicle_objects_all}
    return render(request,'trax_vehicle_manager_data/maintenance_detail.html',data)

def maintenance_details_form_submit(request):
    if request.method == "POST":
        vehicle_number=request.POST['vehicle_number']
        vehicle_detail=request.POST['vehicle_detail']
        bill_date=request.POST['bill_date']
        vehicle_type=request.POST['vehicle_type']
        chalak_malal=request.POST['chalak_malal']
        company_name=request.POST['company_name']
        odometer_reading=request.POST['odometer_reading']
        bill_number=request.POST['bill_number']
        dealer_part_number=request.POST['dealer_part_number']
        maintenance_dealer_name=request.POST['maintenance_dealer_name']
        particular=request.POST['particular']
        particular_details=request.POST['particular_details']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        amount=request.POST['amount']
        discount=request.POST['discountInput']
        tax=request.POST['taxInput']
        tax_float=float(tax)
        tds=request.POST['tdsInput']
        tds_float=float(tds)
        labour_charge=request.POST['labour_charge']
        labour_charge_float=float(labour_charge)
        total_amount=request.POST['total_amount']
        total_amount_float=float(total_amount)
        maintenance_vehicle_id=request.POST['maintenance_vehicle_id']
        Maintenance.objects.create(maintenance_vehicle_id=Vehicles.objects.get(pk=maintenance_vehicle_id),
                                    vehicle_number=vehicle_number,
                                    vehicle_detail=vehicle_detail,
                                    bill_date=bill_date,
                                    vehicle_type=vehicle_type,
                                    chalak_malal=chalak_malal,
                                    company_name=company_name,
                                    odometer_reading=odometer_reading,
                                    bill_number=bill_number,
                                    dealer_part_number=dealer_part_number,
                                    maintenance_dealer_name=maintenance_dealer_name,
                                    particular=particular,
                                    particular_details=particular_details,
                                    quantity=quantity,
                                    rate=rate,
                                    amount=amount,
                                    discount=discount,
                                    tax=tax_float,
                                    tds=tds_float,
                                    labour_charge=labour_charge_float,
                                    total_amount=total_amount_float,
                                    )
        
        return HttpResponseRedirect(reverse('trax_vehicle_manager_data:maintenance_details'))

#Maintenance Summary for one vehicle
@login_required(login_url='/login')
def maintenance_summary_one_vehicle(request,pk):
    if request.method == "POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        all_maintenance_objects = Maintenance.objects.filter(maintenance_vehicle_id=pk).all()
        maintenance_object_filter_by_bill_date = all_maintenance_objects.filter(bill_date__range=[date1,date2]).all()
        km_sum = maintenance_object_filter_by_bill_date.aggregate(Sum('odometer_reading'))
        amount_sum = maintenance_object_filter_by_bill_date.aggregate(Sum('amount'))
        vehicle_number = Vehicles.objects.get(pk=pk).vehicle_number
        pk = Vehicles.objects.get(pk=pk)
        filter_date = "True"
        data={'pk':pk,'date1':date1,'date2':date2,'filter_date':filter_date,'all_maintenance_objects':maintenance_object_filter_by_bill_date,'vehicle_number':vehicle_number,'km_sum':km_sum,'amount_sum':amount_sum}
    else:
        vehicle_number = Vehicles.objects.get(pk=pk).vehicle_number
        all_maintenance_objects = Maintenance.objects.filter(maintenance_vehicle_id=pk).all()
        km_sum = Maintenance.objects.filter(maintenance_vehicle_id=pk).aggregate(Sum('odometer_reading'))
        amount_sum = Maintenance.objects.filter(maintenance_vehicle_id=pk).aggregate(Sum('amount'))
        pk = Vehicles.objects.get(pk=pk)
        data={'pk':pk,'all_maintenance_objects':all_maintenance_objects,'vehicle_number':vehicle_number,'km_sum':km_sum,'amount_sum':amount_sum}
    return render(request,'trax_vehicle_manager_data/view_maintenance_summary_one_vehicle.html',data)

def maintenance_summary_one_company(request,dealer_name):
    if request.method=="POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        all_maintenance_objects = Maintenance.objects.filter(maintenance_dealer_name=dealer_name).all()
        maintenance_object_filter_by_bill_date = all_maintenance_objects.filter(bill_date__range=[date1,date2]).all()
        maintenance_dealer_name = Maintenance.objects.get(maintenance_dealer_name=dealer_name).maintenance_dealer_name
        filter_date = "True"
        data = {'date1':date1,'date2':date2,'filter_date':filter_date,'maintenance_dealer_name':maintenance_dealer_name,'all_maintenance_objects':maintenance_object_filter_by_bill_date}
    else:
        all_maintenance_objects = Maintenance.objects.filter(maintenance_dealer_name=dealer_name).all()
        maintenance_dealer_name = Maintenance.objects.get(maintenance_dealer_name=dealer_name).maintenance_dealer_name
        data = {'maintenance_dealer_name':maintenance_dealer_name,'all_maintenance_objects':all_maintenance_objects}
    return render(request,'trax_vehicle_manager_data/view_maintenance_summary_one_company.html',data)


#Maintenance update payment page view
@login_required(login_url='/login')
def maintenance_update_payment(request):
    maintenanceobjectlist = []
    if request.method == "POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        maintenanceobjectlist = Maintenance.objects.filter(bill_date__range=[date1,date2]).all()
        filter_date = "True"
        data =  {'maintenance_data_objects':maintenanceobjectlist,'date1':date1,'date2':date2,'filter_date':filter_date}
    else:
        maintenanceobjectlist = Maintenance.objects.all()
        data = {'maintenance_data_objects':maintenanceobjectlist}
    return render(request,'trax_vehicle_manager_data/maintenance_update_payment.html',data)

#Maintenance Delete data page view
@login_required(login_url='/login')
def maintenance_delete_data(request):
    maintenanceobjectlist = []
    if request.method == "POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        maintenanceobjectlist = Maintenance.objects.filter(bill_date__range=[date1,date2]).all()
        filter_date = "True"
        data =  {'maintenance_data_objects':maintenanceobjectlist,'date1':date1,'date2':date2,'filter_date':filter_date}
    else:
        maintenanceobjectlist = Maintenance.objects.all()
        data = {'maintenance_data_objects':maintenanceobjectlist}
    return render(request,'trax_vehicle_manager_data/maintenance_delete.html',data)

#Maintenance Delete data within date
#def maintenance_delete_within_date(request):
 #   maintenanceobjectlist = []
  #  if request.method == "POST":
   #     date1=request.POST['date1']
    #    date2=request.POST['date2']
     #   maintenanceobjectlist = Maintenance.objects.filter(bill_date__range=[date1,date2]).delete()
      #  filter_date = "True"
       # data =  {'maintenance_data_objects':maintenanceobjectlist,'date1':date1,'date2':date2,'filter_date':filter_date}
        #return reverse_lazy('trax_vehicle_manager_data:maintenance_delete_data',data)

#Recurring expense PUC page view
def recurring_expense_puc(request):
    puc_objects = PUCRecurringExpenses.objects.all()
    data = {'puc_objects':puc_objects}
    return render(request,'trax_vehicle_manager_data/recurring_expense_puc.html',data)

#Recurring expense OilChange page view
def recurring_expense_oilchange(request):
    oil_Change_objects = OilChangeRecurringExpenses.objects.all()
    data = {'oil_Change_objects':oil_Change_objects}
    return render(request,'trax_vehicle_manager_data/recurring_expense_oilchange.html',data)

#Recurring expense HubGreasing page view
def recurring_expense_hubgreasing(request):
    hub_greasing_objects = HubGreasingRecurringExpenses.objects.all()
    data = {'hub_greasing_objects':hub_greasing_objects}
    return render(request,'trax_vehicle_manager_data/recurring_expense_hubgreasing.html',data)



#Insurance claim page view
def insurance_claim(request):
    return render(request,'trax_vehicle_manager_data/insurance_claim.html')

#Police setlement page view
def police_settlement(request):
    return render(request,'trax_vehicle_manager_data/police_settlement.html')

#Company MIS page view
def mis(request):
    return render(request,'trax_vehicle_manager_data/mis.html')

#Tyres page view
def tyres(request):
    return render(request,'trax_vehicle_manager_data/tyres.html')

#Supervisor For page view
def supervisor_form(requset):
    return render(requset,'trax_vehicle_manager_data/superwisor_form.html')

#Supervisor data page view
def supervisor_data(requset):
    return render(requset,'trax_vehicle_manager_data/supervisor_data.html')

#Profile page view
def profile(requset):
    return render(requset,'trax_vehicle_manager_data/profile.html')

#Report Error page view
def report_error(requset):
    return render(requset,'trax_vehicle_manager_data/report_error.html')

@method_decorator(login_required, name='dispatch')
class Upload_New_Maintenance_Form(BSModalCreateView):
    template_name = 'trax_vehicle_manager_data/upload_maintenance_form.html'
    form_class = MaintenanceForm
    success_message = 'Success: Maintenance Form was Uploaded Successfully.'
    success_url = reverse_lazy('trax_vehicle_manager_data:maintenance_data')

@method_decorator(login_required, name='dispatch')
class MaintenanceUpdateView(BSModalUpdateView):
    model = Maintenance
    template_name = 'trax_vehicle_manager_data/update_data.html'
    form_class = MaintenanceForm
    success_message = 'Success: Maintenance data was updated.'
    success_url = reverse_lazy('trax_vehicle_manager_data:maintenance_data')

@method_decorator(login_required, name='dispatch')
class MaintenanceDeleteView(BSModalDeleteView):
    model = Maintenance
    template_name = 'trax_vehicle_manager_data/delete_data.html'
    success_message = 'Success: Maintenance data was Deleted.'
    success_url = reverse_lazy('trax_vehicle_manager_data:maintenance_data')

@method_decorator(login_required, name='dispatch')
class MaintenanceReadView(BSModalReadView):
    model = Maintenance
    context_object_name = 'maintenance_data'
    template_name = 'trax_vehicle_manager_data/read_maintenance_data.html'   

@method_decorator(login_required, name='dispatch')
class MaintenanceReadOnDeletePageView(BSModalReadView):
    model = Maintenance
    context_object_name = 'maintenance_data'
    template_name = 'trax_vehicle_manager_data/read_maintenance_data_on_delete_page.html'  

@method_decorator(login_required, name='dispatch')
class Create_New_Driver(BSModalCreateView):
    template_name = 'trax_vehicle_manager_data/add_a_new_driver.html'
    form_class = DriverForm
    success_message = 'Success: Driver Data was added Successfully.'
    success_url = reverse_lazy('trax_vehicle_manager_data:driver_master')

@method_decorator(login_required, name='dispatch')
class DriverUpdateView(BSModalUpdateView):
    model = Drivers
    template_name = 'trax_vehicle_manager_data/update_data.html'
    form_class = DriverForm
    success_message = 'Success: Driver data was updated.'
    success_url = reverse_lazy('trax_vehicle_manager_data:driver_master')

@method_decorator(login_required, name='dispatch')
class DriverDeleteView(BSModalDeleteView):
    model = Drivers
    template_name = 'trax_vehicle_manager_data/delete_data.html'
    success_message = 'Success: Driver data was Deleted.'
    success_url = reverse_lazy('trax_vehicle_manager_data:driver_master')

@method_decorator(login_required, name='dispatch')
class DriverOdometerUpdateView(BSModalUpdateView):
    model = Drivers_Odometer_Data
    template_name = 'trax_vehicle_manager_data/update_data.html'
    form_class = DriverOdometerForm
    success_message = 'Success: Driver Odometer data was updated.'
    success_url = reverse_lazy('trax_vehicle_manager_data:driver_odometer')

@method_decorator(login_required, name='dispatch')
class DriverOdometerDeleteView(BSModalDeleteView):
    model = Drivers_Odometer_Data
    template_name = 'trax_vehicle_manager_data/delete_data.html'
    success_message = 'Success: Driver Odometer data was Deleted.'
    success_url = reverse_lazy('trax_vehicle_manager_data:driver_odometer')

@method_decorator(login_required, name='dispatch')
class DieselOdometerReadingUpdateView(BSModalUpdateView):
    model = Diesel
    template_name = 'trax_vehicle_manager_data/update_data.html'
    form_class = DieselOdometerReadingUpdateForm
    success_message = 'Success: Diesel Odometer Reading was updated.'
    success_url = reverse_lazy('trax_vehicle_manager_data:full_diesel_details_filtered_by_date')

@method_decorator(login_required, name='dispatch')
class Upload_Diesel_Data_Form(BSModalCreateView):
    template_name = 'trax_vehicle_manager_data/upload_diesel_data_form.html'
    form_class = DieselDataForm
    success_message = 'Success: Diesel Data was Uploaded Successfully.'
    success_url = reverse_lazy('trax_vehicle_manager_data:full_diesel_details_filtered_by_date')

@method_decorator(login_required, name='dispatch')
class DriverKYCFormReadView(BSModalReadView):
    model = Drivers
    context_object_name = 'driver_kyc_data'
    template_name = 'trax_vehicle_manager_data/read_driver_kyc_data.html'   

@method_decorator(login_required, name='dispatch')
class VehicleUpdateView(BSModalUpdateView):
    model = Vehicles
    template_name = 'trax_vehicle_manager_data/update_data.html'
    form_class = VehicleDataForm
    success_message = 'Success: Vehicle data was updated.'
    success_url = reverse_lazy('trax_vehicle_manager_data:vehicles')

@method_decorator(login_required, name='dispatch')
class VehicleDeleteView(BSModalDeleteView):
    model = Vehicles
    template_name = 'trax_vehicle_manager_data/delete_data.html'
    success_message = 'Success: Vehicle data was Deleted.'
    success_url = reverse_lazy('trax_vehicle_manager_data:vehicles')

@method_decorator(login_required, name='dispatch')
class Create_New_Vehicle(BSModalCreateView):
    template_name = 'trax_vehicle_manager_data/add_a_new_vehicle.html'
    form_class = VehicleDataForm
    success_message = 'Success: Vehicles Data was added Successfully.'
    success_url = reverse_lazy('trax_vehicle_manager_data:vehicles')

class RecurringExpensePUCUpdateView(BSModalUpdateView):
    model = PUCRecurringExpenses
    template_name = 'trax_vehicle_manager_data/update_data.html'
    form_class = PUCDataForm
    success_message = 'Success: PUC data was updated.'
    success_url = reverse_lazy('trax_vehicle_manager_data:recurring_expense_puc')

class RecurringExpenseOilChangeUpdateView(BSModalUpdateView):
    model = OilChangeRecurringExpenses
    template_name = 'trax_vehicle_manager_data/update_data.html'
    form_class = OilChangeForm
    success_message = 'Success: Oil Change data was updated.'
    success_url = reverse_lazy('trax_vehicle_manager_data:recurring_expense_oilchange')

class RecurringExpenseHubGreasingUpdateView(BSModalUpdateView):
    model = HubGreasingRecurringExpenses
    template_name = 'trax_vehicle_manager_data/update_data.html'
    form_class = HubGreasingForm
    success_message = 'Success: Hub Greasing data was updated.'
    success_url = reverse_lazy('trax_vehicle_manager_data:recurring_expense_hubgreasing')

class RecurringExpensePUCDeleteView(BSModalDeleteView):
    model = PUCRecurringExpenses
    template_name = 'trax_vehicle_manager_data/delete_data.html'
    success_message = 'Success: PUC data was Deleted.'
    success_url = reverse_lazy('trax_vehicle_manager_data:recurring_expense_puc')

class RecurringExpenseOilChangeDeleteView(BSModalDeleteView):
    model = OilChangeRecurringExpenses
    template_name = 'trax_vehicle_manager_data/delete_data.html'
    success_message = 'Success: Oil Change data was Deleted.'
    success_url = reverse_lazy('trax_vehicle_manager_data:recurring_expense_oilchange')

class RecurringExpenseHubGreasingDeleteView(BSModalDeleteView):
    model = HubGreasingRecurringExpenses
    template_name = 'trax_vehicle_manager_data/delete_data.html'
    success_message = 'Success: Hub Greasing data was Deleted.'
    success_url = reverse_lazy('trax_vehicle_manager_data:recurring_expense_hubgreasing')

class RecurringExpensePUCCreateView(BSModalCreateView):
    template_name = 'trax_vehicle_manager_data/add_a_new_puc.html'
    form_class = PUCDataForm
    success_message = 'Success: PUC Data was added Successfully.'
    success_url = reverse_lazy('trax_vehicle_manager_data:recurring_expense_puc')

class RecurringExpenseOilChangeCreateView(BSModalCreateView):
    template_name = 'trax_vehicle_manager_data/add_a_new_oilchange.html'
    form_class = OilChangeForm
    success_message = 'Success: Oil Change Data was added Successfully.'
    success_url = reverse_lazy('trax_vehicle_manager_data:recurring_expense_oilchange')

class RecurringExpenseHubGreasingCreateView(BSModalCreateView):
    template_name = 'trax_vehicle_manager_data/add_a_new_hubgreasing.html'
    form_class = HubGreasingForm
    success_message = 'Success: Hub Greasing Data was added Successfully.'
    success_url = reverse_lazy('trax_vehicle_manager_data:recurring_expense_hubgreasing')
