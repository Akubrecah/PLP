#Staff & Patient Records -Key-value pairs for instant lookups
# Staff Directory (ID → Details)
staff = {
    101: {"name": "Dr. Smith", "role": "Cardiologist", "station": "ER"},
    202: {"name": "Nurse Lee", "role": "ICU", "station": "Ward 3B"},
    303: {"name": "Dr. Patel", "role": "Radiologist", "station": "Lab 2"}
}

# Patient Records (ID → Medical History)
patients = {
    "P881": {"name": "John Munae", "allergies": ["Penicillin"], "ward": "ICU"},
    "P882": {"name": "Maria Garcia", "allergies": ["Smoke"], "ward": "Ward 4A"}
}

# Access data
print("Cardiologist on duty:", staff[101]['name'])  # Dr. Smith
print("John's allergies:", patients["P881"]["allergies"])  # ['Penicillin']

# Add new patient
patients["P883"] = {"name": "Alex Kim", "allergies": ["Latex"], "ward": "ER"}

print("Nurse on Duty:", staff[202]['name'])  # Nurse Lee
# Output: Nurse Lee
print("Garcia's allergies:", patients["P882"]["allergies"])  # ['Smoke']
# Update staff role
staff[303]["role"] = "Chief Radiologist"
print("Updated Radiologist Role:", staff[303]["role"])  # Chief Radiologist
# Output: Chief Radiologist
# Remove a patient record
del patients["P881"]
print("Remaining Patients:", patients)  # {'P882': {'name': 'Maria Garcia