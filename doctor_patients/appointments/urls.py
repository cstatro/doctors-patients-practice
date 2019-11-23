from django.urls import path
from .views import AppointmentsList

urlpatterns = [path('appointments', AppointmentsList.as_view())]
