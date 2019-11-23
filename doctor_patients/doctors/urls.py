from django.urls import path
from .views import DoctorListView, DoctorView

urlpatterns = [path('doctors', DoctorListView.as_view()),
               path('doctor/<int:pk>', DoctorView.as_view())
               ]
