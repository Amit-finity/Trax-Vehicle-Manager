from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.managers import InheritanceManager
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):
    '''Overrides the custom django user model'''
    # Datafields
    System_administrator = 1
    Boss = 2
    Office_Team = 3
    ROLE_CHOICES = (
        (Office_Team,'Office Team'),
        (Boss,'Boss'),
        (System_administrator,'System administrator')
    )
    
    #Here i defined user role
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=System_administrator)



class Drivers(models.Model):
        driver_reference_no = models.IntegerField()
        driver_driver_name = models.CharField(max_length=264,default="")
        driver_vehicle_short_number = models.CharField(max_length=12,blank=True)
        driver_vehicle_number = models.CharField(max_length=12,blank=True)
        driver_vehicle_type = models.CharField(max_length=264,blank=True)
        vehicle_type_of_module = models.CharField(max_length=264,blank=True)
        driver_joining_date = models.DateTimeField(default=timezone.now)
        driver_license_number = models.CharField(max_length=264,blank=True)
        driver_aadhar_number = models.CharField(max_length=264,blank=True,default="")
        driver_contact_number = models.CharField(max_length=264,blank=True,default="")
        driver_pan_number = models.CharField(max_length=264,blank=True,default="")
        driver_address_proof = models.CharField(max_length=264,blank=True,default="")
        driver_photoid_proof = models.CharField(max_length=264,blank=True,default="")
        driver_driver_bank_name = models.CharField(max_length=264,default="")
        driver_bank_name = models.CharField(max_length=264,blank=True,default="")
        driver_bank_account_number = models.CharField(max_length=264,blank=True)
        driver_ban_ifsc_code = models.CharField(max_length=264,blank=True,default="")
        driver_bank_branch = models.CharField(max_length=264,blank=True,default="")
        driver_alternate_contact_number=models.CharField(max_length=264,blank=True,default="")
        driver_license_residence_address=models.CharField(max_length=264,blank=True,default="")
        driver_aadhar_card_residence_address=models.CharField(max_length=264,blank=True,default="")
        driver_years_of_experience = models.CharField(max_length=264,blank=True,default="")
        driver_last_employer_name = models.CharField(max_length=264,blank=True,default="")
        driver_years_with_kruze_or_aaron = models.CharField(max_length=264,blank=True,default="")

        def __str__(self):
                return str(self.driver_reference_no)

class Cleaners(models.Model):
        cleaner_Id = models.PositiveSmallIntegerField() 
        cleaner_Name = models.CharField(max_length=20)
        cleaner_Age = models.IntegerField()
        cleaner_License_Number = models.IntegerField()
        cleaner_Address = models.CharField(max_length=20)
        cleaner_Contact_Number = models.IntegerField()
        cleaner_Salary = models.IntegerField()

        def __str__(self):
                return str(self.pk)

        class Meta:
                verbose_name_plural = "Cleaners Master List"
                verbose_name = "Cleaner"

class Vehicles(models.Model):
        vehicle_id = models.CharField(max_length=900,blank=True)
        vehicle_number = models.CharField(max_length=900,blank=True)
        vehicle_card_number = models.CharField(max_length=900,blank=True)
        vehicle_seating_capacity = models.CharField(max_length=900,blank=True)
        minimum_average = models.CharField(max_length=900,blank=True)
        incremental_average = models.CharField(max_length=900,blank=True)
        vehicle_current_status = models.CharField(max_length=900,blank=True)
        vehicle_buying_date = models.DateTimeField(blank=True)
        vehicle_type = models.CharField(max_length=900,blank=True)
        vehicle_ownership = models.CharField(max_length=900,blank=True)
        vehicle_ownership_details = models.CharField(max_length=900,blank=True)
        vehicle_manufacturer = models.CharField(max_length=900,blank=True)
        vehicle_registered_number = models.CharField(max_length=900,blank=True)

        # Relationship of Vehicle with Drivers and Cleaners
        driver_id = models.ForeignKey(Drivers, on_delete = models.CASCADE)
        cleaner_id = models.ForeignKey(Cleaners, on_delete = models.CASCADE)

        def __str__(self):
            return (self.vehicle_card_number)

        class Meta:
                verbose_name_plural = "Vehicles Master List"
                verbose_name = "Vehicle"

class Expenses(models.Model):
    expense_name = models.CharField(max_length=50)
    expense_id = models.PositiveSmallIntegerField()
    
    
    def __str__(self):
        return str(self.pk)

#Child class of Expenses
class Diesel(Expenses):
    terminal_id = models.PositiveSmallIntegerField()
    transaction_date = models.DateTimeField()
    merchant = models.CharField(max_length=50)
    account_number = models.IntegerField()
    card_used = models.CharField(max_length=50)
    vehicle_number = models.IntegerField()
    vehicle_detail = models.CharField(max_length=50)
    transaction_type = models.CharField(max_length=50)
    diesel_rate = models.IntegerField()
    volume = models.IntegerField()
    amount_Rs = models.PositiveIntegerField()
    balance_Rs = models.PositiveIntegerField()
    odometer_reading = models.PositiveIntegerField()
    ownership = models.CharField(max_length=50)

    def __str__(self):
                return str(self.pk)

#Child class of Expenses
class Maintenance(Expenses):
    YES = 'yes'
    NO = 'no'
    chalak_malak_choices = ((YES,'yes'),(NO,'no'))
    vehicle_number = models.PositiveIntegerField()
    vehicle_detail = models.CharField(max_length=50)
    bill_date = models.DateTimeField()
    vehicle_type = models.CharField(max_length=50)
    chalak_malal = models.CharField(choices=chalak_malak_choices,max_length=100)
    company_name = models.CharField(max_length=50)
    odometer_reading = models.PositiveIntegerField()
    bill_number = models.PositiveIntegerField()
    dealer_part_number = models.PositiveIntegerField()
    particular = models.CharField(max_length=50)
    particular_details = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    tax = models.PositiveIntegerField()
    tds = models.PositiveIntegerField()
    labour_charge = models.PositiveIntegerField()	
    total_amount = models.PositiveIntegerField()

    def __str__(self):
                return str(self.pk)

#Child class of Maintenance
class GarageBilling(Maintenance):
    def __str__(self):
                return str(self.pk)

#Child class of Maintenance
class Insurance(Maintenance):
    def __str__(self):
                return str(self.pk)


#Child class of Maintenance
class PoliceSettlements(Maintenance):
    def __str__(self):
                return str(self.pk)

#Child class of Expenses
class RecurringExpenses(Expenses):
    def __str__(self):
                return str(self.pk)

#Child class of RecurringExpenses
class PUC(RecurringExpenses):
    def __str__(self):
                return str(self.pk)

#Child class of RecurringExpenses
class OilChange(RecurringExpenses):
    def __str__(self):
                return str(self.pk)

class Client(models.Model):

    client_name = models.CharField(max_length=200)
    client_address = models.TextField(blank=True)

    def __str__(self):
        return str(self.pk)

class Drivers_Odometer_Data(models.Model):
        drivers_odometer_data_date_of_entry = models.DateTimeField(default=timezone.now)
        drivers_odometer_data_driver_id = models.ForeignKey(Drivers, on_delete = models.CASCADE)
        drivers_odometer_data_mobile_number = models.CharField(max_length=12,blank=True)
        drivers_odometer_data_vehicle_number = models.ForeignKey(Vehicles, on_delete = models.CASCADE,blank=True, null=True)
        drivers_odometer_data_odometer_kilometer = models.CharField(max_length=12,blank=True)
        drivers_odometer_data_cleaner_id = models.ForeignKey(Cleaners, on_delete = models.CASCADE,blank=True, null=True)

        def __str__(self):
                return str(self.pk)
        
        class Meta:
                verbose_name_plural = "Drivers Odometer List"
                verbose_name = "Driver's Odometer"