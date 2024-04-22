from django.urls import path,include
from rest_framework import routers
from .views import DroneViewSet
router=routers.DefaultRouter()
router.register('drones',DroneViewSet)
urlpatterns=[
    path('',include(router.urls))
]