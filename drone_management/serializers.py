from rest_framework import serializers
from .models import Drone,Camera, Weapon,AttackDrone,Mission,MissionDrones
class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drone
        fields='__all__'
        #fields=['id','model','type']

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Camera
        fields='__all__'
class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model=Weapon
        fields='__all__'

class AttackDroneSerializer(serializers.ModelSerializer):
    class Meta:
        model=AttackDrone
        fields='__all__'

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mission
        fields='__all__'

class MissionDronesSerializer(serializers.ModelSerializer):
    class Meta:
        model=MissionDrones
        fields='__all__'

