from django import forms
from .models import HealthRecord

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['name', 'Age', "Fever", "Fatigue", "Chills or Sweating", "Loss of Appetite", "Cough", 
    "Shortness of Breath", "Sore Throat", "Runny or Stuffy Nose", "Nausea or Vomiting", 
    "Diarrhea", "Abdominal Pain", "Headache", "Body Aches & Muscle Pain", 
    "Joint Pain or Stiffness", "Chest Pain", "Throat Pain", "Ear Pain", 
    "Eye Pain or Sensitivity", "Dizziness or Lightheadedness", 
    "Nerve Pain (Tingling, Burning, Sharp Pain)", "Rash or Skin Changes", 
    "Swollen Lymph Nodes", "Pregnancy", "Injury concerning bone"]

