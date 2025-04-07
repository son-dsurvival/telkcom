# from flask import Flask, render_template, request, jsonify
# import pandas as pd
# import joblib
# import requests

# app = Flask(__name__)

# # Load model and encoder
# model = joblib.load('model.pkl')
# label_encoder = joblib.load('label_encoder.pkl')

# # Symptoms list
# symptoms = [
#     'Fever', 'Fatigue', 'Chills or Sweating', 'Loss of Appetite', 'Cough', 'Shortness of Breath', 
#     'Sore Throat', 'Runny or Stuffy Nose', 'Nausea or Vomiting', 'Diarrhea', 'Abdominal Pain', 
#     'Headache', 'Body Aches & Muscle Pain', 'Joint Pain or Stiffness', 'Chest Pain', 'Throat Pain', 
#     'Ear Pain', 'Eye Pain or Sensitivity', 'Dizziness or Lightheadedness', 'Nerve Pain (Tingling, Burning, Sharp Pain)', 
#     'Rash or Skin Changes', 'Swollen Lymph Nodes', 'Pregnancy', 'Injury concerning bone',
# ]

# @app.route('/')
# def index():
#     return render_template('form.html', symptoms=symptoms)

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         # Collect form data
#         name = request.form.get('name')
#         age = request.form.get('age')
        
#         # Collect responses for each symptom
#         responses = {symptom: request.form.get(symptom, 'no') for symptom in symptoms}
#         responses['Age'] = age
        
#         # Create DataFrame for prediction
#         df = pd.DataFrame([responses])
        
        
#         # Convert symptoms to binary (1 for yes, 0 for no)
        
#         for column in symptoms:
#             df[column] = df[column].map({'yes': 1, 'no': 0})
        
#         # Make prediction
#         prediction = model.predict(df)
#         original_value = label_encoder.inverse_transform(prediction)
        
        
#         # Return prediction and webhook status
#         return render_template('result.html', 
#                               name=name,
#                               age=age, 
#                               prediction=original_value,
#                                 )
# if __name__ == '__main__':
#     app.run(debug=True)