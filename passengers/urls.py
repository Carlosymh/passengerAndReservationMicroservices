from django.urls import path
from . import views

urlpatterns = [
    path('getPassengers/', views.GetPassengers),
    path('createPassengers/', views.CreatePassengers),
    path('updatePassenger/<int:pk>', views.UpdatePassenger),
    path('deletePassenger/<int:pk>', views.DeletePassenger),
]