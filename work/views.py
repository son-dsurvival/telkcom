from django.shortcuts import render
from django.views import View
from .forms import HealthRecordForm
import pandas as pd
import joblib
from email.message import EmailMessage
import ssl
import smtplib


class HealthRecordView(View):
    # GET request handler
    def get(self, request):
        form = HealthRecordForm()
        return render(request, 'form.html', {'form': form})

    # POST request handler
    def post(self, request):
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            data = form.cleaned_data
            symptom_dict = {
                'Fever': data['Fever'],
                'Fatigue': data['Fatigue'],
                'Chills or Sweating': data['Chills or Sweating'],
                'Loss of Appetite': data['Loss of Appetite'],
                'Cough': data['Cough'],
                'Shortness of Breath': data['Shortness of Breath'],
                'Sore Throat': data['Sore Throat'],
                'Runny or Stuffy Nose': data['Runny or Stuffy Nose'],
                'Nausea or Vomiting': data['Nausea or Vomiting'],
                'Diarrhea': data['Diarrhea'],
                'Abdominal Pain': data['Abdominal Pain'],
                'Headache': data['Headache'],
                'Body Aches & Muscle Pain': data['Body Aches & Muscle Pain'],
                'Joint Pain or Stiffness': data['Joint Pain or Stiffness'],
                'Chest Pain': data['Chest Pain'],
                'Throat Pain': data['Throat Pain'],
                'Ear Pain': data['Ear Pain'],
                'Eye Pain or Sensitivity': data['Eye Pain or Sensitivity'],
                'Dizziness or Lightheadedness': data['Dizziness or Lightheadedness'],
                'Nerve Pain (Tingling, Burning, Sharp Pain)': data['Nerve Pain (Tingling, Burning, Sharp Pain)'],
                'Rash or Skin Changes': data['Rash or Skin Changes'],
                'Swollen Lymph Nodes': data['Swollen Lymph Nodes'],
                'Pregnancy': data['Pregnancy'],
                'Injury concerning bone': data['Injury concerning bone'],
                'Age': data['Age']
}
            name = data['name']
            Fever = data['Fever']
            Fatigue = data['Fatigue']
            Chills_or_Sweating = data['Chills or Sweating']
            Loss_of_Appetite = data['Loss of Appetite']
            Cough = data['Cough']
            Shortness_of_Breath = data['Shortness of Breath']
            Sore_Throat = data['Sore Throat']
            Runny_or_Stuffy_Nose = data['Runny or Stuffy Nose']
            Nausea_or_Vomiting = data['Nausea or Vomiting']
            Diarrhea = data['Diarrhea']
            Abdominal_Pain = data['Abdominal Pain']
            Headache = data['Headache']
            Body_Aches_Muscle_Pain = data['Body Aches & Muscle Pain']
            Joint_Pain_or_Stiffness = data['Joint Pain or Stiffness']
            Chest_Pain = data['Chest Pain']
            Throat_Pain = data['Throat Pain']
            Ear_Pain = data['Ear Pain']
            Eye_Pain_or_Sensitivity = data['Eye Pain or Sensitivity']
            Dizziness_or_Lightheadedness = data['Dizziness or Lightheadedness']
            Nerve_Pain = data['Nerve Pain (Tingling, Burning, Sharp Pain)']
            Rash_or_Skin_Changes = data['Rash or Skin Changes']
            Swollen_Lymph_Nodes = data['Swollen Lymph Nodes']
            Pregnancy = data['Pregnancy']
            Injury_concerning_bone = data['Injury concerning bone']
            age= data['Age']
            df= pd.DataFrame([symptom_dict])
            r=self.work(df)
            self.email(Fever, Fatigue, Chills_or_Sweating, Loss_of_Appetite, Cough, Shortness_of_Breath, Sore_Throat, Runny_or_Stuffy_Nose, Nausea_or_Vomiting, Diarrhea, Abdominal_Pain, Headache, Body_Aches_Muscle_Pain, Joint_Pain_or_Stiffness, Chest_Pain, Throat_Pain, Ear_Pain, Eye_Pain_or_Sensitivity, Dizziness_or_Lightheadedness, Nerve_Pain, Rash_or_Skin_Changes, Swollen_Lymph_Nodes, Pregnancy, Injury_concerning_bone)
            # Optionally, you can redirect to a success page or show a success message
            return render(request, 'result.html', {'name':name,'result':r,'age':age
})
        return render(request, 'form.html', {'form': form})
    def work(self,df):
        model = joblib.load('model.pkl')
        label_encoder = joblib.load('label_encoder.pkl')
        
        symptoms = [
            'Fever', 'Fatigue', 'Chills or Sweating', 'Loss of Appetite', 'Cough', 'Shortness of Breath', 
            'Sore Throat', 'Runny or Stuffy Nose', 'Nausea or Vomiting', 'Diarrhea', 'Abdominal Pain', 
            'Headache', 'Body Aches & Muscle Pain', 'Joint Pain or Stiffness', 'Chest Pain', 'Throat Pain', 
            'Ear Pain', 'Eye Pain or Sensitivity', 'Dizziness or Lightheadedness', 'Nerve Pain (Tingling, Burning, Sharp Pain)', 
            'Rash or Skin Changes', 'Swollen Lymph Nodes', 'Pregnancy', 'Injury concerning bone', 
        ]
        for column in symptoms:
            if column != 'age':  # Skip 'age' since it's numeric
                # Ensure the values match the expected 'yes'/'no'
                df[column] = df[column].map({'yes': 1, 'no': 0}).astype(int)
        prediction = model.predict(df)
        original_value = label_encoder.inverse_transform(prediction)
        print(original_value[0])
        return original_value[0]
    def email( self,Fever, Fatigue, Chills_or_Sweating, Loss_of_Appetite, Cough, Shortness_of_Breath, Sore_Throat, Runny_or_Stuffy_Nose, Nausea_or_Vomiting, Diarrhea, Abdominal_Pain, Headache, Body_Aches_Muscle_Pain, Joint_Pain_or_Stiffness, Chest_Pain, Throat_Pain, Ear_Pain, Eye_Pain_or_Sensitivity, Dizziness_or_Lightheadedness, Nerve_Pain, Rash_or_Skin_Changes, Swollen_Lymph_Nodes, Pregnancy, Injury_Concerning_Bone,
):
        smtp_server = "smtp.gmail.com"
        smtp_port = 465
        sender_email = "oyeneyinfemisayo@gmail.com"
        receiver_email = "femiayo2.0@gmail.com"
        password = 'vcrt miah mhba qkro'

        subject='hey'
        body= f"""fever {Fever}, fatigue {Fatigue}, chills_or_sweating {Chills_or_Sweating}, 
        loss_of_appetite {Loss_of_Appetite}, cough {Cough}, shortness_of_breath {Shortness_of_Breath}, 
        sore_throat {Sore_Throat}, runny_or_stuffy_nose {Runny_or_Stuffy_Nose}, nausea_or_vomiting {Nausea_or_Vomiting}, 
        diarrhea {Diarrhea}, abdominal_pain {Abdominal_Pain}, headache {Headache}, 
        body_aches_muscle_pain {Body_Aches_Muscle_Pain}, joint_pain_or_stiffness {Joint_Pain_or_Stiffness}, 
        chest_pain {Chest_Pain}, throat_pain {Throat_Pain}, ear_pain {Ear_Pain}, 
        eye_pain_or_sensitivity {Eye_Pain_or_Sensitivity}, dizziness_or_lightheadedness {Dizziness_or_Lightheadedness}, 
        nerve_pain {Nerve_Pain}, rash_or_skin_changes {Rash_or_Skin_Changes}, swollen_lymph_nodes {Swollen_Lymph_Nodes}, 
        pregnancy {Pregnancy}, injury_concerning_bone {Injury_Concerning_Bone}

"""
        em = EmailMessage()
        em['From']= sender_email
        em['To']= receiver_email
        em ['Subject']= subject
        em.set_content(body) 

        contexts=ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server,smtp_port, context=contexts) as smtp:
            smtp.login(sender_email,password)
            smtp.send_message(em)
