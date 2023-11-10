from flask import Flask, jsonify, request
from flask_restful import  Resource, Api
import requests

app = Flask(__name__)

# In-memory data storage for demonstration purposes
patient_records = {
    "123456": {
        "patientID": "123456",
        "name": "John Doe",
        "dob": "1980-01-01",
        "diagnosis": "Initial diagnosis details",
        "treatmentPlans": []
    }
}

# Service URLs
PATIENT_RECORD_SERVICE_URL = "http://localhost:5001"
APPOINTMENT_SERVICE_URL = "http://localhost:5002"
BILLING_SERVICE_URL = "http://localhost:5003"


# Endpoint to get patient record
@app.route('/patient-records/<patient_id>', methods=['GET'])
def get_patient_record(patient_id):
    if patient_id in patient_records:
        return jsonify(patient_records[patient_id])
    else:
        return jsonify({"error": "Patient not found"}), 404

# Endpoint to update diagnosis
@app.route('/patient-records/<patient_id>/diagnosis', methods=['PUT'])
def update_diagnosis(patient_id):
    if patient_id in patient_records:
        data = request.get_json()
        patient_records[patient_id]["diagnosis"] = data["diagnosis"]
        return jsonify({"message": "Diagnosis updated successfully"})
    else:
        return jsonify({"error": "Patient not found"}), 404

# Endpoint to add treatment plan
@app.route('/patient-records/<patient_id>/treatment-plans', methods=['POST'])
def add_treatment_plan(patient_id):
    if patient_id in patient_records:
        data = request.get_json()
        treatment_plan = {
            "planID": str(len(patient_records[patient_id]["treatmentPlans"]) + 1),
            "description": data["description"]
        }
        patient_records[patient_id]["treatmentPlans"].append(treatment_plan)
        return jsonify(treatment_plan)
    else:
        return jsonify({"error": "Patient not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
