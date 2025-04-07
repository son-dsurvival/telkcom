
# import pandas as pd
# import joblib

# # Load model with joblib
# model = joblib.load('model.pkl')
# label_encoder = joblib.load('label_encoder.pkl')



# symptoms = [
#     'Fever', 'Fatigue', 'Chills or Sweating', 'Loss of Appetite', 'Cough', 'Shortness of Breath', 
#     'Sore Throat', 'Runny or Stuffy Nose', 'Nausea or Vomiting', 'Diarrhea', 'Abdominal Pain', 
#     'Headache', 'Body Aches & Muscle Pain', 'Joint Pain or Stiffness', 'Chest Pain', 'Throat Pain', 
#     'Ear Pain', 'Eye Pain or Sensitivity', 'Dizziness or Lightheadedness', 'Nerve Pain (Tingling, Burning, Sharp Pain)', 
#     'Rash or Skin Changes', 'Swollen Lymph Nodes', 'Pregnancy', 'Injury concerning bone', 
# ]

# responses = {}

# for symptom in symptoms:
#     responses[symptom] = input(f'Do you have {symptom}? (yes/no): ')
#     if responses[symptom]=='yes':
#         responses[symptom]='yes'
#     else:
#         responses[symptom]='no'

# responses['Age']= input(f'Do you have age? ').strip()
# print(responses)
# df= pd.DataFrame([responses])
# for column in symptoms:
#     if column != 'age':  # Skip 'age' since it's numeric
#         # Ensure the values match the expected 'yes'/'no'
#         df[column] = df[column].map({'yes': 1, 'no': 0}).astype(int)
# prediction = model.predict(df)
# original_value = label_encoder.inverse_transform(prediction)
# print("Prediction:",original_value )



