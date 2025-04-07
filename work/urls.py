from django.urls import path
from .views import HealthRecordView

urlpatterns = [
    path('',HealthRecordView.as_view(), name='work'),
]