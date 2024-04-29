from rest_framework import serializers
from .models import Drone,Camera, MissionType, Weapon,AttackDrone,Mission,MissionDrones,DroneType
class DroneSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=DroneType.choices)
    class Meta:
        model=Drone
        fields='__all__'
        #fields=['id','model','type']

class CameraSerializer(serializers.ModelSerializer):
    #type = serializers.ChoiceField(choices=Camera._meta.get_field('type').choices)
    #resolution = serializers.ChoiceField(choices=Camera._meta.get_field('resolution').choices)
    #lenses_type = serializers.ChoiceField(choices=Camera._meta.get_field('lenses_type').choices)
    class Meta:
        model=Camera
        fields='__all__'
class WeaponSerializer(serializers.ModelSerializer):
    #caliber = serializers.ChoiceField(choices=Weapon._meta.get_field('caliber').choices)
    #range = serializers.ChoiceField(choices=Weapon._meta.get_field('range').choices)
    class Meta:
        model=Weapon
        fields='__all__'

class AttackDroneSerializer(serializers.ModelSerializer):
    weapon = WeaponSerializer()
    class Meta:
        model=AttackDrone
        fields='__all__'

class MissionSerializer(serializers.ModelSerializer):
    #type = serializers.ChoiceField(choices=MissionType.choices)
    #drones=DroneSerializer(many=True)
    class Meta:
        model=Mission
        fields='__all__'

class MissionDronesSerializer(serializers.ModelSerializer):
    #drone=DroneSerializer()
    #Mission=MissionSerializer()
    #role = serializers.CharField()
    class Meta:
        model=MissionDrones
        fields='__all__'

