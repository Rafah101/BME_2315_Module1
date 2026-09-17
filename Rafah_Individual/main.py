from patient import Patient
import matplotlib.pyplot as plt
import pandas as pd
import statistics

# Loads the csv file and saves it into the dataframe variable 'df'
df = pd.read_csv('Dataset/Metadata and Protein Data for Module 1.csv')

# Transforms DataFrame rows into a collection of structured Patient objects. Each object encapsulates demographic details, pathology scores (Thal/Braak), and quantifiable protein measurements.
def create_patients_from_dataframe(df):
    patients = []
    for index, row in df.iterrows():
        patient = Patient(
            donor_id=row['Donor ID'],
            age_at_death=row['Age at Death'],
            sex=row['Sex'],
            education=row['Highest level of education'],
            years_education=row['Years of education'],
            genotype=row['APOE Genotype'],
            cognitive_status=row['Cognitive Status'],
            age_onset=row['Age of onset cognitive symptoms'],
            age_diagnosis=row['Age of Dementia diagnosis'],
            thal=row['Thal'],
            braak=row['Braak'],
            abeta40=row['ABeta40 pg/ug'],
            abeta42=row['ABeta42 pg/ug'],
            ttau=row['tTAU pg/ug'],
            ptau=row['pTAU pg/ug']
        )
        patients.append(patient)
    return patients

# Convert CSV records into a list of Patient instances
def main():
    patients = create_patients_from_dataframe(df)
    sort_by_age = sorted(patients, key=lambda p: p.age_at_death, reverse=True)
    for p in sort_by_age:
        print(p)
    print()
    female_dementia = Patient.filter_patients(patients, sex='Female', cognitive_status='Dementia')
    print(f"Number of female patients with dementia: {len(female_dementia)}")
    for p in female_dementia:
        print(p)
    print()

    dementia_patients = Patient.filter_patients(patients, cognitive_status='Dementia')
    female_abeta42 = [p.abeta42 for p in dementia_patients if p.sex == 'Female']
    male_abeta42 = [p.abeta42 for p in dementia_patients if p.sex == 'Male']
    means = [statistics.mean(female_abeta42), statistics.mean(male_abeta42)]

    stdevs = [statistics.stdev(female_abeta42), statistics.stdev(male_abeta42)]
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.bar(['Female', 'Male'], means, yerr=stdevs, capsize=5, color=['pink',
    'lightblue'])
    ax.set_ylabel('Mean Abeta42 (pg/ug)')
    ax.set_title('Mean Abeta 42 Levels by Sex in Dementia Patients (+/- SD)')
    plt.tight_layout()
    plt.show()
    # Creates the Scatter Plot
    ages = [p.age_at_death for p in patients]
    abeta42_all = [p.abeta42 for p in patients]
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.scatter(ages, abeta42_all, color='purple', alpha=0.6)
    ax.set_xlabel('Age at Death')
    ax.set_ylabel('Abeta42 (pg/ug)')
    ax.set_title('Abeta 42 Levels vs Age at Death')
    plt.tight_layout()
    plt.show()

# Required to make graphs appear when running the script directly. This block ensures that the main function is executed only when the script is run as the main program, and not when it is imported as a module in another script.
if __name__ == "__main__":
    main()