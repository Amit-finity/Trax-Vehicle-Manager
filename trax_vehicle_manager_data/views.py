from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)


from trax_vehicle_manager_data.models import Drivers,Vehicles,Cleaners,Drivers_Odometer_Data,Expenses,Maintenance
from trax_vehicle_manager_data.forms import MaintenanceForm

from django.db.models import Sum

# Create your views here.
#<----------------- Authentication Views --------------------

#Login Page view
def login(request):
    return render(request,'trax_vehicle_manager_data/login.html')

#Register Page view
def register(request):
    return render(request,'trax_vehicle_manager_data/register.html')

#forget password view
def forgetpassword(request):
    return render(request,'trax_vehicle_manager_data/forget_password.html')

#</----------------- Authentication Views --------------------


#<----------------- Projects Pages  Views --------------------

#Vehicle page view
def vehicles(request):
    return render(request,'trax_vehicle_manager_data/vehicles.html')

#Driver master page view
def driver_master(request):
    driver_master_objects = Drivers.objects.all()
    data = {'driver_master_list':driver_master_objects}
    return render(request,'trax_vehicle_manager_data/driver_master.html',data)

#Driver Odometer view
def driver_odometer(request):
    driver_odometer_objects = Drivers_Odometer_Data.objects.all()
    data = {'driver_odometer_list': driver_odometer_objects}
    return render(request,'trax_vehicle_manager_data/driver_odometer.html',data)

#Driver Usage page view
def drivers_usage(request):
    driver_objects = Drivers.objects.all()
    data = {'driver_objects':driver_objects}
    return render(request,'trax_vehicle_manager_data/driver_usage.html',data)

#Drivers Details Page View
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
    data = {'driver_odometer_filered_based_on_driver_pk':driver_odometer_filered_based_on_driver_pk,'driver_odometer_km_average_dict':driver_odometer_km_average_dict}
    return render(request,'trax_vehicle_manager_data/driver_detail.html',data)

#Driver Odometer form page view
def drivers_odometer_form(request):
    Drivers_dict = Drivers.objects.all()
    vehicles_dict = Vehicles.objects.all()
    Cleaners_dict = Cleaners.objects.all()
    data = {'drivers':Drivers_dict,'vehicles':vehicles_dict,'cleaners':Cleaners_dict}
    return render(request,'trax_vehicle_manager_data/driver_form.html',data)

#Driver Odometer form submit page view
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
def drivers_odometer_successfull_form(request):
    return render(request,'trax_vehicle_manager_data/driver_successfull_message.html')

#Full diesel details page view
def full_diesel_details(request):
    return render(request,'trax_vehicle_manager_data/full_diesel_details.html')

#Diesel transaction details page view
def diesel_transaction_details(request):
    return render(request,'trax_vehicle_manager_data/diesel_transaction_details.html')

#Diesel transaction tally page view
def transaction_tally(request):
    return render(request,'trax_vehicle_manager_data/diesel_transaction_tally.html')

#Diesel delete data page view
def diesel_delete_data(request):
    return render(request,'trax_vehicle_manager_data/diesel_delete.html')

#Maintenance Data page view
def maintenance_data(request):
    maintenance_data_objects = Maintenance.objects.all()
    data = {'maintenance_data_objects':maintenance_data_objects}
    return render(request,'trax_vehicle_manager_data/maintenance_data.html',data)

#Maintenance Details page view
def maintenance_details(request):
    """ maintenance_data_objects = Maintenance.objects.all()
    maintenance_details_monthly_expense_total_dict = {}
    maintenance_details_vehicle_km_dict = {}
    maintenance_objects = Maintenance.objects.filter(expense_vehicle_id=Vehicles.objects.get(pk=pk)).all()
    total_expense_per_vehicle = 0
    total_km_per_vehicle = 0
    for maintenance in maintenance_objects:
        total_expense_per_vehicle = total_expense_per_vehicle + maintenance.amount
        total_km_per_vehicle = total_km_per_vehicle + maintenance.odometer_reading
        maintenance_details_monthly_expense_total_dict[maintenance.pk]=total_expense_per_vehicle
        maintenance_details_vehicle_km_dict[maintenance.pk]=total_km_per_vehicle

        ItemPrice.objects.aggregate(Sum('price'))
    data = {'maintenance_data_objects':maintenance_data_objects,'maintenance_details_monthly_expense_total_dict':maintenance_details_monthly_expense_total_dict,'maintenance_details_vehicle_km_dict':maintenance_details_vehicle_km_dict} """
    vehicle_dict = {}
    vehicle_objects_all = Vehicles.objects.all()
    for one_vehicle_object in vehicle_objects_all:
        km_sum = Maintenance.objects.filter(expense_vehicle_id=one_vehicle_object.pk).aggregate(Sum('odometer_reading'))
        amount_sum = Maintenance.objects.filter(expense_vehicle_id=one_vehicle_object.pk).aggregate(Sum('amount'))
        vehicle_dict[one_vehicle_object] = km_sum,amount_sum
    data = {'vehicle_dict':vehicle_dict}
    return render(request,'trax_vehicle_manager_data/maintenance_detail.html',data)

#Maintenance update payment page view
def maintenance_update_payment(request):
    maintenance_data_objects = Maintenance.objects.all()
    data = {'maintenance_data_objects':maintenance_data_objects}
    return render(request,'trax_vehicle_manager_data/maintenance_update_payment.html',data)

#Maintenance Delete data page view
def maintenance_delete_data(request):
    maintenance_data_objects = Maintenance.objects.all()
    data = {'maintenance_data_objects':maintenance_data_objects}
    return render(request,'trax_vehicle_manager_data/maintenance_delete.html',data)

#Recurring expense page view
def recurring_expense(request):
    return render(request,'trax_vehicle_manager_data/recurring_expense.html')

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

class Upload_New_Maintenance_Form(BSModalCreateView):
    template_name = 'trax_vehicle_manager_data/upload_maintenance_form.html'
    form_class = MaintenanceForm
    success_message = 'Success: Maintenance Form was Uploaded Successfully.'
    success_url = reverse_lazy('trax_vehicle_manager_data:maintenance_data')

class MaintenanceUpdateView(BSModalUpdateView):
    model = Maintenance
    template_name = 'trax_vehicle_manager_data/update_data.html'
    form_class = MaintenanceForm
    success_message = 'Success: Maintenance data was updated.'
    success_url = reverse_lazy('trax_vehicle_manager_data:maintenance_data')

class MaintenanceDeleteView(BSModalDeleteView):
    model = Maintenance
    template_name = 'trax_vehicle_manager_data/delete_data.html'
    success_message = 'Success: Maintenance data was Deleted.'
    success_url = reverse_lazy('trax_vehicle_manager_data:maintenance_data')

class MaintenanceReadView(BSModalReadView):
    model = Maintenance
    context_object_name = 'maintenance_data'
    template_name = 'trax_vehicle_manager_data/read_maintenance_data.html'   

class MaintenanceReadOnDeletePageView(BSModalReadView):
    model = Maintenance
    context_object_name = 'maintenance_data'
    template_name = 'trax_vehicle_manager_data/read_maintenance_data_on_delete_page.html'  