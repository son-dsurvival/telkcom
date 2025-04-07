from django.db import models

# Create your models here.
class HealthRecord(models.Model):
    Fever = models.CharField(name="Fever", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Fatigue = models.CharField(name="Fatigue", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Chills_or_Sweating = models.CharField(name="Chills or Sweating", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Loss_of_Appetite = models.CharField(name="Loss of Appetite", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Cough = models.CharField(name="Cough", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Shortness_of_Breath = models.CharField(name="Shortness of Breath", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Sore_Throat = models.CharField(name="Sore Throat", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Runny_or_Stuffy_Nose = models.CharField(name="Runny or Stuffy Nose", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Nausea_or_Vomiting = models.CharField(name="Nausea or Vomiting", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Diarrhea = models.CharField(name="Diarrhea", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Abdominal_Pain = models.CharField(name="Abdominal Pain", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Headache = models.CharField(name="Headache", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Body_Aches_Muscle_Pain = models.CharField(name="Body Aches & Muscle Pain", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Joint_Pain_or_Stiffness = models.CharField(name="Joint Pain or Stiffness", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Chest_Pain = models.CharField(name="Chest Pain", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Throat_Pain = models.CharField(name="Throat Pain", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Ear_Pain = models.CharField(name="Ear Pain", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Eye_Pain_or_Sensitivity = models.CharField(name="Eye Pain or Sensitivity", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Dizziness_or_Lightheadedness = models.CharField(name="Dizziness or Lightheadedness", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Nerve_Pain = models.CharField(name="Nerve Pain (Tingling, Burning, Sharp Pain)", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Rash_or_Skin_Changes = models.CharField(name="Rash or Skin Changes", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Swollen_Lymph_Nodes = models.CharField(name="Swollen Lymph Nodes", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Pregnancy = models.CharField(name="Pregnancy", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)
    Injury_Concerning_Bone = models.CharField(name="Injury concerning bone", choices=[("yes", "yes"), ("no", "no")], default="no", max_length=3)



    # General fields for user information
    name = models.CharField(max_length=100)
    age = models.IntegerField(name="Age")
    def __str__(self):
        return self.name
    