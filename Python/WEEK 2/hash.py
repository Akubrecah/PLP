# Doctor Authentication System
import hashlib

# Database of Doctors (Hash Map: Username → Hashed Password + Details)
doctors_db = {
    # Format: {username: {"password_hash": "...", "name": "...", "department": "..."}}
    "dr_strange": {
        "password_hash": hashlib.sha256("Spell@2024".encode()).hexdigest(),
        "name": "Stephen Strange",
        "department": "Neurosurgery"
    },
    "dr_house": {
        "password_hash": hashlib.sha256("Lupus!123".encode()).hexdigest(),
        "name": "Gregory House",
        "department": "Diagnostics"
    }
}

# Patient Records (Secured behind authentication)
patient_records = {
    "ICU-101": {"name": "Tony Stark", "condition": "Shrapnel injury"},
    "ER-205": {"name": "Bruce Banner", "condition": "Gamma radiation exposure"}
}

def register_doctor(username: str, password: str, name: str, department: str):
    """Add new doctor with hashed password"""
    if username in doctors_db:
        print("⚠️ Username already exists!")
        return False
    
    # Create password hash (add salt in real systems!)
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    doctors_db[username] = {
        "password_hash": password_hash,
        "name": name,
        "department": department
    }
    print(f"✅ {name} registered in {department}!")
    return True

def doctor_login(username: str, password: str):
    """Authenticate doctor using hash comparison"""
    if username not in doctors_db:
        print("❌ User not found")
        return False
    
    # Hash the attempt
    attempt_hash = hashlib.sha256(password.encode()).hexdigest()
    stored_hash = doctors_db[username]["password_hash"]
    
    if attempt_hash == stored_hash:
        print(f"🔓 Access granted! Welcome Dr. {doctors_db[username]['name']}")
        return True
    else:
        print("❌ Invalid password")
        return False

def access_patient_record(username: str, patient_id: str):
    """Securely access patient data after auth"""
    if doctor_login(username, input("Password: ")):
        record = patient_records.get(patient_id)
        if record:
            print(f"\n📝 Patient {patient_id}:")
            for key, value in record.items():
                print(f"  {key.capitalize()}: {value}")
        else:
            print("⚠️ Record not found")
    else:
        print("🚫 Access denied to patient records")

# Demo Workflow
if __name__ == "__main__":
    # Register new doctor
    register_doctor(
        username="dr_grey",
        password="Heal$oul123",
        name="Meredith Grey",
        department="General Surgery"
    )
    
    # Attempt login
    print("\n[ Login Attempt ]")
    doctor_login("dr_strange", "Spell@2024")  # Correct → Success
    doctor_login("dr_house", "wrong!pass")    # Incorrect → Failure
    
    # Access patient data (simulate)
    print("\n[ Access Patient Record ]")
    access_patient_record("dr_strange", "ICU-101")