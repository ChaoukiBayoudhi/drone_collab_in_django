from rest_framework import viewsets
from .models import Drone,Camera,Weapon,AttackDrone,Mission,MissionDrones
from .serializers import DroneSerializer,CameraSerializer,WeaponSerializer,AttackDroneSerializer,MissionSerializer,MissionDronesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

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
    #get the missions of a given drone
    @action(methods=['GET'],detail=True)
    def get_drone_missions(self,request,id=None):
        if request.method!='GET':
            return Response({'message':'This endpoint only supports GET requests','status':status.HTTP_405_METHOD_NOT_ALLOWED})
        try:
            drone=Drone.objects.get(pk=id)
        except Drone.DoesNotExist:
            return Response({'message':'Drone not found','status':status.HTTP_404_NOT_FOUND})
        missions=Mission.objects.filter(drones=drone)
        missions_serialized=MissionSerializer(missions,many=True)
        return Response(missions_serialized.data)
    
   # def 
        
        

