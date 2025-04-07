# from flask import Flask, render_template, request,jsonify
# import requests

# app = Flask(__name__)

# symptom_list = [
#     'Fever', 'Fatigue', 'Chills or Sweating', 'Loss of Appetite', 'Cough', 'Shortness of Breath',
#     'Sore Throat', 'Runny or Stuffy Nose', 'Nausea or Vomiting', 'Diarrhea', 'Abdominal Pain',
#     'Headache', 'Body Aches & Muscle Pain', 'Joint Pain or Stiffness', 'Chest Pain', 'Throat Pain',
#     'Ear Pain', 'Eye Pain or Sensitivity', 'Dizziness or Lightheadedness', 'Nerve Pain (Tingling, Burning, Sharp Pain)',
#     'Rash or Skin Changes', 'Swollen Lymph Nodes', 'Pregnancy', 'Injury concerning bone',
# ]

# @app.route('/')
# def index():
#     return render_template('form.html', symptoms=symptom_list)

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         age= request.form.get('age')
#         responses = {'age':age,'name':name, **{symptom: request.form.get(symptom, 'No') for symptom in symptom_list}}  # Default to 'No' if missing
#     WEBHOOK_URL='http://localhost:5678/webhook-test/18967999-4aed-4d17-b289-a69e2f7a46af'

#     response = requests.post(WEBHOOK_URL, json=responses)

#     # Return response
#     if response.status_code == 200:
#         return jsonify({"message": "Data sent successfully", "status": response.status_code}), 200
#     else:
#         return jsonify({"message": "Failed to send data", "status": response.status_code, "error": response.text}), 400
# if __name__ == '__main__':
#     app.run(debug=True)