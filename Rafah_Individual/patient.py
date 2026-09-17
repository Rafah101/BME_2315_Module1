class Patient:
# Initializes a Patient instance with the provided attributes
    def __init__(self, donor_id, age_at_death, sex, education, years_education,
    genotype, cognitive_status, age_onset, age_diagnosis, thal, braak, abeta40,
    abeta42, ttau, ptau):
        self.donor_id = donor_id
        self.age_at_death = age_at_death
        self.sex = sex
        self.education = education
        self.years_education = years_education
        self.genotype = genotype
        self.cognitive_status = cognitive_status
        self.age_onset = age_onset
        self.age_diagnosis = age_diagnosis
        self.thal = thal
        self.braak = braak
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ttau = ttau
        self.ptau = ptau

# Returns a string representation of the Patient instance for easy debugging and display
    def __repr__(self):
        return f"Patient(donor_id={self.donor_id}, age_at_death= {self.age_at_death}, sex={self.sex}, education={self.education}, years_education= {self.years_education}, genotype={self.genotype}, cognitive_status= {self.cognitive_status}, age_onset={self.age_onset}, age_diagnosis= {self.age_diagnosis}, thal={self.thal}, braak={self.braak}, abeta40={self.abeta40}, abeta42={self.abeta42}, ttau={self.ttau}, ptau={self.ptau})"

# Filters a list of Patient instances based on the provided criteria (sex, cognitive_status, genotype, min_thal)
    @classmethod
    def filter_patients(cls, patients, sex=None, cognitive_status=None, genotype=None, min_thal=None):
        matches = []
        for i in patients:
            if (sex != None and i.sex != sex):
                continue
            if (cognitive_status != None and i.cognitive_status != cognitive_status):
                continue
            if (genotype != None and i.genotype != genotype):
                continue
            if (min_thal != None and (i.thal is None or i.thal < min_thal)):
                continue
            matches.append(i)
        return matches