from patient import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
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
 

"""
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

"""
 
male_apoe44 = Patient.filter(Patient.all_patients, sex="Male", apoe="4_4")
print(f"\nNumber of male patients with APOE 4_4 = {len(male_apoe44)}")
 
eighties = Patient.filter_by_range(Patient.all_patients, "age_at_death", 80, 89)
eighties_high_thal = Patient.filter_by_range(eighties, "thal", minimum=4)
print(f"Patients who died in their 80s with a Thal score > 3 = {len(eighties_high_thal)}")

patients_with_mmse = Patient.filter_by_range(Patient.all_patients, "Last MMSE Score", minimum=0)
 
abeta42 = np.array([p.get_abeta42() for p in patients_with_mmse])
mmse = np.array([p.get_last_mmse() for p in patients_with_mmse])
 
print(f"Patients with a recorded MMSE score: {len(patients_with_mmse)}")
 
# --- Fit the model ---
X = abeta42.reshape(-1, 1)   # sklearn needs a 2D array for the predictor
y = mmse
 
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
 
slope = model.coef_[0]
intercept = model.intercept_
r2 = r2_score(y, y_pred)
