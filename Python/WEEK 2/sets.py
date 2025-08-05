#Equipment Tracking & Sterilization -Unique items for contamination control
# Sterilized equipment sets
sterile_lab_equipment = {"Microscope", "Centrifuge", "Pipettes"}
sterile_er_equipment = {"Stethoscope", "Defibrillator", "Sutures"}

# Contaminated items
contaminated = {"Defibrillator", "Sutures", "Scalpel"}

# Sterilize ER equipment
sterile_er_equipment -= contaminated
print("Sterile ER Equipment:", sterile_er_equipment)  
# Output: {'Stethoscope'}

# Combine all sterile tools
all_sterile = sterile_lab_equipment | sterile_er_equipment
print("All Sterile Equipment:", all_sterile)  
# Output: {'Microscope', 'Centrifuge', 'Pipettes', 'Stethoscope'}

print("Contaminated Lab Equipment:", contaminated)
# Output: set() (no contaminated items in lab equipment)