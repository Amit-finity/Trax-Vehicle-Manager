#<------- imported libraries ----------
#django admin
from django.contrib import admin

#path,include
from django.urls import path

#</------- imported libraries ---------


#<-------- importing view -------------

from trax_vehicle_manager_data import views

#</-------- importing view ------------

#App Name Of Project
app_name='trax_vehicle_manager_data'

urlpatterns = [
    #Create your URLs here.

    #<----------- Authentication URLs ---------------

    #url for login page
    path('login',views.login,name='login'),
    
    #url for Register page
    path('register',views.register,name='register'),

    #url for forgot password page
    path('forgetpassword',views.forgetpassword,name='forgetpassword'),
    
    #</----------- Authentication URLs ---------------


    #<------------ Projects Page URLs ----------------

    #url for vehicle list page
    path('vehicles',views.vehicles,name='vehicles'),
    
    #url for driver master page
    path('driver/driver_master',views.driver_master,name='driver_master'),

    #url for add a new driver Create_New_Driver
    path('driver/driver_master/create',views.Create_New_Driver.as_view(),name='driver_master_create'),

    #url for update a driver in driver master
    path('driver/driver_master/update_driver_data/<int:pk>', views.DriverUpdateView.as_view(), name='update_driver_data'),   

    #url for delete a driver in driver master
    path('driver/driver_master/delete_driver_data/<int:pk>', views.DriverDeleteView.as_view(), name='delete_driver_data'),

    #url for driver odometer page
    path('driver/driver_odometer',views.driver_odometer,name='driver_odometer'),

    #url for driver odometer update view 
    path('driver/driver_odometer/update_driver_odometer_data/<int:pk>', views.DriverOdometerUpdateView.as_view(), name='update_driver_odometer_data'),

    #url for driver odometer delete view 
    path('driver/driver_odometer/delete_driver_odometer_data/<int:pk>', views.DriverOdometerDeleteView.as_view(), name='delete_driver_odometer_data'),

    #url for driver Usage page
    path('driver/drivers_usage',views.drivers_usage,name='drivers_usage'),

    #url for driver Details page
    path('driver/drivers_details/<int:pk>',views.drivers_details,name='drivers_details'),
    
    #url for driver form page
    path('',views.drivers_odometer_form,name='drivers_odometer_form'),
    
    #url for driver form submit page
    path('drivers_odometer_form_submit',views.drivers_odometer_form_submit,name='drivers_odometer_form_submit'),
    
    #url for driver successfull message form page
    path('driver/drivers_odometer_successfull_form',views.drivers_odometer_successfull_form,name='drivers_odometer_successfull_form'),
    
    #url for Diesel details page
    path('diesel/full_diesel_details',views.full_diesel_details,name='full_diesel_details'),

    #url for Full Diesel details page filtered by date
    path('diesel/full_diesel_details_filtered_by_date',views.full_diesel_details_filtered_by_date,name='full_diesel_details_filtered_by_date'),

    #url for Diesel Transaction details page
    path('diesel/diesel_transaction_details',views.diesel_transaction_details,name='diesel_transaction_details'),
    
    #url for vehicle diesel report page
    path('diesel/vehicle_diesel_report',views.vehicle_diesel_report,name='vehicle_diesel_report'),
    
    #url for Diesel Transaction Tally page
    path('diesel/transaction_tally',views.transaction_tally,name='transaction_tally'),
    
    #url for Diesel delete page
    path('diesel/diesel_delete_data',views.diesel_delete_data,name='diesel_delete_data'),    

    #url for Maintenance data page
    path('maintenance/maintenance_data',views.maintenance_data,name='maintenance_data'),
    
    #url for Upload Maintenance Form
    path('maintenance/upload_maintenance_form', views.Upload_New_Maintenance_Form.as_view(), name='upload_maintenance_form'),

    #url for Read Maintenance Data
    path('maintenance/read_maintenance_data/<int:pk>', views.MaintenanceReadView.as_view(), name='read_maintenance_data'),

    #url for Update Maintenance Data
    path('maintenance/update_maintenance_data/<int:pk>', views.MaintenanceUpdateView.as_view(), name='update_maintenance_data'),    

    #url for Delete Maintenance Data
    path('maintenance/delete_maintenance_data/<int:pk>', views.MaintenanceDeleteView.as_view(), name='delete_maintenance_data'),    

    #url for maintenance details page
    path('maintenance/maintenance_details/',views.maintenance_details,name='maintenance_details'),
    
    #url for maintenance update payment page
    path('maintenance/maintenance_update_payment',views.maintenance_update_payment,name='maintenance_update_payment'),

    
    #url for Read Maintenance Data on Delete Page
    path('maintenance/read_maintenance_data_on_delete_page/<int:pk>', views.MaintenanceReadOnDeletePageView.as_view(), name='read_maintenance_data_on_delete_page'),

    #url for Diesel delete page
    path('maintenance/maintenance_delete_data',views.maintenance_delete_data,name='maintenance_delete_data'),    

    #url for recurring expense page
    path('recurring_expense',views.recurring_expense,name='recurring_expense'),
    
    #url for insurance claim page
    path('settlement/insurance_claim',views.insurance_claim,name='insurance_claim'),
    
    #url for police settlement page
    path('settlement/police_settlement',views.police_settlement,name='police_settlement'),
   
    #url for mis page
    path('mis',views.mis,name='mis'),
    
    #url for tyres page
    path('tyres',views.tyres,name='tyres'),
   
    #url for supervisor form page
    path('supervisor/supervisor_form',views.supervisor_form,name='supervisor_form'),
   
    #url for supervisor data page
    path('supervisor/supervisor_data',views.supervisor_data,name='supervisor_data'),
    
    #url for supervisor data page
    path('profile',views.profile,name='profile'),
   
    #url for report error page
    path('report_error',views.report_error,name='report_error'),

    #</------------ Projects Page URLs ----------------
   
]
