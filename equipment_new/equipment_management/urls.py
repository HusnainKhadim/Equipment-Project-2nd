from django.urls import path
from . import views

urlpatterns=[
  path('',views.sign_in, name='sign_in'),
  path('create_equipment_objects/', views.equipment_objects_creation, name='equipment_objects_creation'),
]
