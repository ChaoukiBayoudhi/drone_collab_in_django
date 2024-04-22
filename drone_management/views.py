from rest_framework import viewsets
from .models import Drone,Camera,Weapon,AttackDrone,Mission,MissionDrones
from .serializers import DroneSerializer,CameraSerializer,WeaponSerializer,AttackDroneSerializer,MissionSerializer,MissionDronesSerializer
# Create your views here.
#implement the CRUD operations on Drone using the ModelViewSet DRF class
class DroneViewSet(viewsets.ModelViewSet):
    queryset=Drone.objects.all()
    serializer_class=DroneSerializer
    #http_method_names=['GET','POST']

class CameraViewSet(viewsets.ModelViewSet):
    queryset=Camera.objects.all()
    serializer_class=CameraSerializer

class WeaponViewSet(viewsets.ModelViewSet):
    queryset=Weapon.objects.all()
    serializer_class=WeaponSerializer

class AttackDroneViewSet(viewsets.ModelViewSet):
    queryset=AttackDrone.objects.all()
    serializer_class=AttackDroneSerializer

class MissionViewSet(viewsets.ModelViewSet):
    queryset=Mission.objects.all()
    serializer_class=MissionSerializer

class MissionDronesViewSet(viewsets.ModelViewSet):
    queryset=MissionDrones.objects.all()
    serializer_class=MissionDronesSerializer

