from rest_framework import viewsets
from .models import Drone
from .serializers import DroneSerializer
# Create your views here.
#implement the CRUD operations on Drone using the ModelViewSet DRF class
class DroneViewSet(viewsets.ModelViewSet):
    queryset=Drone.objects.all()
    serializer_class=DroneSerializer
    #http_method_names=['GET','POST']