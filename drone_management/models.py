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

    def __str__(self):
        return f'{self.model}-{self.id}'

class Camera(models.Model):
    type=models.CharField(max_length=50,choices=[('NORMAL','normal camera'),('INFRARED','infrared camera'),('THERMAL','thermal camera')])
    resolution=models.CharField(max_length=50,choices=[('LOW','low resolution'),('MEDIUM','medium resolution'),('HIGH','high resolution')])
    lenses_type=models.CharField(max_length=50,choices=[('TELEPHOTO','telephoto'),('WIDE_ANGLE','wide angule'),('MACRO','macro')])
    #relationship between Camera and Drone (n-1)
    drone=models.ForeignKey(Drone, on_delete=models.CASCADE)
    class Meta:
        db_table='cameras' 
    
    def __str__(self) -> str:
        return f'{self.id} - {self.type}'
    
class Weapon(models.Model):
    caliber=models.CharField(max_length=50,choices=[('SMALL','small caliber'),('MEDIUM','medium caliber'),('LARGE','large caliber')],default='SMALL')
    range=models.PositiveIntegerField(default=0)

    class Meta:
        db_table='weapons'
    def __str__(self):
        return f'{self.id}-{self.caliber}-{self.range}'

class AttackDrone(Drone):
    weapon=models.OneToOneField(Weapon,on_delete=models.CASCADE)#,primary_key=True)
    class Meta:
        db_table='attack_drones'
    def __str__(self):
        return super().__str__()+f'weapon: {self.weapon.id}'
    
class MissionType(models.TextChoices):
    MONITORING='MN','Monitoring'
    RESCUE='RS','Rescue'
    DELIVRY='DL','Delivery'
    SEARCH='SC','Search'
    OTHER='OT','Other'

class Mission(models.Model):
    name=models.CharField(max_length=100, unique=True)
    objectives=models.TextField()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    #area_to_cover=PolygonField()
    area_to_cover=models.TextField()
    type=models.CharField(max_length=50,choices=MissionType.choices,default=MissionType.MONITORING)
    #relationship between Mission and Drone (n-n)
    drones=models.ManyToManyField(Drone,through='MissionDrones',through_fields=['mission','drone'])
    class Meta:
        db_table='missions'

    def __str__(self):
        return f'{self.name}-{self.type}'
    
class MissionDrones(models.Model):
    drone=models.ForeignKey(Drone,on_delete=models.CASCADE)
    mission=models.ForeignKey(Mission,on_delete=models.CASCADE)
    role=models.CharField(max_length=50)
    class Meta:
        db_table='mission_drones'
        unique_together=[('drone','mission')]

    def __str__(self):
        return f'{self.drone.id}-{self.mission.id}-{self.role}'

