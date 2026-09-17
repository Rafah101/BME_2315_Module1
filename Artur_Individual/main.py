from patient import *
import matplotlib.pyplot as plt
import numpy as np
import statistics
import csv

FILEPATH = "/Users/arturdiakiv/Desktop/BME 2315/module 1/BME_2315_Module1/DataSet/Metadata and Protein Data for Module 1.csv"

"""
with open(FILEPATH, newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    headers = next(reader)
    for h in headers:
        print(h)
"""

Patient.instantiate_from_csv(FILEPATH)
 
print(f"Number of patients loaded: {len(Patient.all_patients)}")
print(Patient.all_patients[0])
print(f"Mean age at death = {Patient.mean_age_at_death()}")
 

Patient.all_patients.sort(key=Patient.get_age_at_death, reverse=False)
 
print("\n--- Patients sorted by age at death ---")
for patient in Patient.all_patients:
    print(patient)
 
female_dementia = Patient.filter(Patient.all_patients,
                                 sex="Female",
                                 cognitive_status="Dementia")
 
print(f"\n--- Female patients with dementia (n = {len(female_dementia)}) ---")
for patient in female_dementia:
    print(patient)
 
male_apoe44 = Patient.filter(Patient.all_patients, sex="Male", apoe="4_4")
print(f"\nNumber of male patients with APOE 4_4 = {len(male_apoe44)}")
 
eighties = Patient.filter_by_range(Patient.all_patients, "age_at_death", 80, 89)
eighties_high_thal = Patient.filter_by_range(eighties, "thal", minimum=4)
print(f"Patients who died in their 80s with a Thal score > 3 = {len(eighties_high_thal)}")
 

abeta42_female = []
abeta42_male = []
 
for patient in Patient.filter(Patient.all_patients, sex="Female", cognitive_status="Dementia"):
    abeta42_female.append(patient.abeta42)
 
for patient in Patient.filter(Patient.all_patients, sex="Male", cognitive_status="Dementia"):
    abeta42_male.append(patient.abeta42)
 
x_female_bar = statistics.mean(abeta42_female)
x_male_bar = statistics.mean(abeta42_male)
 
abeta42_female_stdev = statistics.stdev(abeta42_female)
abeta42_male_stdev = statistics.stdev(abeta42_male)
 
print(f"\nFemale mean ABeta42 = {x_female_bar}, stdev = {abeta42_female_stdev}, n = {len(abeta42_female)}")
print(f"Male mean ABeta42 = {x_male_bar}, stdev = {abeta42_male_stdev}, n = {len(abeta42_male)}")
 
sex_cols = ["Female", "Male"]
mean_sex = [x_female_bar, x_male_bar]
stdev_sex = [abeta42_female_stdev, abeta42_male_stdev]
yerr = [np.zeros(len(mean_sex)), stdev_sex]
 
plt.bar(sex_cols, mean_sex, yerr=yerr, capsize=10, color=["pink", "blue"])
plt.title("Mean Amyloid-Beta 42 in Patients with Dementia")
plt.xlabel("Sex")
plt.ylabel("ABeta42 (pg/ug)")
plt.show()
 
age_at_death_list = []
abeta42_list = []
 
for patient in Patient.all_patients:
    age_at_death_list.append(patient.age_at_death)
    abeta42_list.append(patient.abeta42)
 
X = age_at_death_list     # Independent variable
y = abeta42_list          # Dependent variable
 
plt.scatter(X, y, color="blue")
plt.xlabel("Age at Death (years)")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Scatter Plot of ABeta42 vs. Age at Death")
plt.show()