from django.urls import path,include
from rest_framework import routers
from .views import DroneViewSet,CameraViewSet,WeaponViewSet,AttackDroneViewSet,MissionViewSet,MissionDronesViewSet
router=routers.DefaultRouter()
router.register('drones',DroneViewSet)
router.register('cameras',CameraViewSet)
router.register('weapons',WeaponViewSet)
router.register('attack-drones',AttackDroneViewSet)
router.register('missions',MissionViewSet)
router.register('mission-drones',MissionDronesViewSet)
urlpatterns=[
    path('',include(router.urls)),
    path('drone-missions/<int:id>',MissionDronesViewSet.as_view({'get':'get_drone_missions'}))
]