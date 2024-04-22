from rest_framework import serializers
from .models import Drone,Camera
class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drone
        fields='__all__'
        #fields=['id','model','type']

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Camera
        fields='__all__'