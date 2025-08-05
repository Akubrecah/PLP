#Medication Dispensing -Last-In-First-Out (LIFO) for efficient medicine access
# Pharmacy Medication Stack
medication_stack = []

# Stock medications (newest on top)
medication_stack.append("Antibiotics")
medication_stack.append("Painkillers")
medication_stack.append("Insulin")
medication_stack.append("Vitamins")
medication_stack.append("Antacids")
medication_stack.append("Cough Syrup")
medication_stack.append("Allergy Medication")
medication_stack.append("Bandages")
medication_stack.append("Thermometer")
medication_stack.append("First Aid Kit")

print("Pharmacy Stock:", medication_stack)  
# Output: ['Antibiotics', 'Painkillers', 'Insulin']

# Dispense medications
# for _ in range(2):
#     dispensed = medication_stack.pop()
#     print(f"Dispensed: {dispensed} → Remaining: {medication_stack}")