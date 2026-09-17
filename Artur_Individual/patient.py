import csv


class Patient:

    all_patients = []

    def __init__(self, donor_id: str, age_at_death: int, sex: str,
                 education_years: int, apoe: str, cognitive_status: str,
                 age_of_dementia_dx: float, thal: int, braak: str,
                 abeta40: float, abeta42: float, ttau: float, ptau: float):

        self.donor_id = donor_id
        self.age_at_death = age_at_death
        self.sex = sex
        self.education_years = education_years
        self.apoe = apoe
        self.cognitive_status = cognitive_status
        self.age_of_dementia_dx = age_of_dementia_dx
        self.thal = thal
        self.braak = braak
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ttau = ttau
        self.ptau = ptau

        Patient.all_patients.append(self)

    def __repr__(self):
        return (f"{self.donor_id}: ({self.sex} | {self.cognitive_status} | "
                f"age at death: {self.age_at_death} | APOE: {self.apoe} | "
                f"Thal: {self.thal} | ABeta42: {self.abeta42})")

    # ---------- instance methods ("getters") ----------

    def get_age_at_death(self):
        return self.age_at_death

    def get_abeta42(self):
        return self.abeta42

    def get_thal(self):
        return self.thal

    def get_education_years(self):
        return self.education_years

    # ---------- class methods ----------

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        """Open the patient .csv file and make one Patient object per row."""
        with open(filename, encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)

        for row in rows_of_patients:

            if row["Age of Dementia diagnosis"] == "":
                dementia_dx = None
            else:
                dementia_dx = float(row["Age of Dementia diagnosis"])

            Patient(
                donor_id=row["Donor ID"],
                age_at_death=int(row["Age at Death"]),
                sex=row["Sex"],
                education_years=int(row["Years of education"]),
                apoe=row["APOE Genotype"],
                cognitive_status=row["Cognitive Status"],
                age_of_dementia_dx=dementia_dx,
                thal=int(row["Thal"].split()[1]),
                braak=row["Braak"],
                abeta40=float(row["ABeta40 pg/ug"]),
                abeta42=float(row["ABeta42 pg/ug"]),
                ttau=float(row["tTAU pg/ug"]),
                ptau=float(row["pTAU pg/ug"])
            )

    @classmethod
    def get_patient(cls, donor_id):
        for patient in Patient.all_patients:
            if patient.donor_id == donor_id:
                return patient

    @classmethod
    def mean_age_at_death(cls):
        total = 0
        for patient in Patient.all_patients:
            total += patient.age_at_death
        return total / len(Patient.all_patients)

    @classmethod
    def filter(cls, patient_list, sex: str = "any", apoe: str = "any",
               cognitive_status: str = "any", thal: int = "any",
               braak: str = "any", donor_id: str = "any"):
        patients = patient_list
        remove_list = []

        attr_list = (sex, apoe, cognitive_status, thal, braak, donor_id)
        attr_name = ("sex", "apoe", "cognitive_status", "thal", "braak", "donor_id")

        for attr in range(len(attr_list)):
            if attr_list[attr] != "any":
                for patient in patients:
                    if getattr(patient, attr_name[attr]) != attr_list[attr]:
                        remove_list.append(patient)
                patients = [p for p in patients if p not in remove_list]
                remove_list.clear()

        return patients

    @classmethod
    def filter_by_range(cls, patient_list, attribute: str,
                        minimum: float = None, maximum: float = None):
        patients = []
        for patient in patient_list:
            value = getattr(patient, attribute)
            if value is None:
                continue
            if minimum is not None and value < minimum:
                continue
            if maximum is not None and value > maximum:
                continue
            patients.append(patient)
        return patients