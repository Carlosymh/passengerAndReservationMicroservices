from django.urls import path
from . import views

urlpatterns = [
    path('getReservations/', views.GetReservations),
    path('createReservation/', views.CreateReservation),
    path('updateReservation/<int:pk>', views.UpdateReservation),
    path('deleteReservation/<int:pk>', views.DeleteReservation),
]