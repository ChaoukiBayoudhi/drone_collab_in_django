from django.db import models

class DroneType(models.TextChoices):
    #list Of possibility
    #The left member is the value stored in the database and using in the code
    #The right member is the value displayed in the admin interface
    MONITORING='MN','Monitoring Drone'
    DELIVRY='DL','Delivery Drone'
    AGRICULTURE='AG','Agriculture Drone'
    OTHER='OT','Other'

class Drone(models.Model):
    manufacturer=models.CharField(max_length=100,unique=True)
    model=models.CharField(max_length=100)
    #lattitude=models.FloatField()
    lattitude=models.DecimalField(max_digits=10,decimal_places=8)
    longitude=models.DecimalField(max_digits=10,decimal_places=8)
    batteryLevel=models.FloatField(default=100)
    playloadCapacity=models.FloatField(default=0)
    #photo=models.ImageField(upload_to='drone_photos',null=True,blank=True)
    max_flight_time=models.DurationField()
    max_speed=models.FloatField(default=0)
    max_range=models.FloatField(default=0)
    type=models.CharField(max_length=2,choices=DroneType.choices,default=DroneType.MONITORING)
    #inner class could be added to each model
    #it must be located just after the last field definition
    #the class provides some extra information like
    # the table name using db_table property
    #
    class Meta:
        verbose_name='Drone'
        verbose_name_plural='Drones'
        db_table='drones'
        ordering=['model'] #asc order
        #ordering=['-manufacturer','-model'] #desc order

