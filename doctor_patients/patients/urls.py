from django.urls import path
from .views import *

urlpatterns = [path('patients', PatientsListView.as_view())]
