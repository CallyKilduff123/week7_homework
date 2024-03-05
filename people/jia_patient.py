from people.patient import Patient

# base class to patient
# need to assess risk of uveitis so 'import' the name age and condition from superclass
# make the condition JIA
# constructor to initialise the risk factors

class JiaPatient(Patient):
    def __init__(self, name, age, ana_status, age_of_onset, joints_involved, appointments):
        super().__init__(name, age, "JIA")
        self.ana_status = ana_status
        self.age_of_onset = age_of_onset
        self.joints_involved = joints_involved
        self.risk_level = self.calculate_risk()
        self.appointments = appointments

    # method to calculate risk based on risk factors
    # if 1 risk factor - child for screening programme

    def calculate_risk(self):
        risk_factors = 0
        if self.age_of_onset < 7:
            risk_factors += 1
        if self.ana_status:
            risk_factors += 1
        if self.joints_involved <= 4:
            risk_factors += 1
        if risk_factors >= 1:
            return "High"
        else:
            return "Low"

    # method to add appointments to determine next appointment interval
    def add_appointment(self):
        self.appointments += 1



# class ScreeningSchedule:
#     def __init__(self):
#         self.patients_for_screening = []

    # def add_patient(self, jia_patient):
    #     if jia_patient.risk_level == "High":
    #         self.patients_for_screening.append(jia_patient)
    #         print(f"High-risk patient added to uveitis screening schedule: {jia_patient.name}"
    #               f"Screen every 2 months for 6 months.\n"
    #               f"Then screen every 3-4 months until the child turns 12.")
    #     else:
    #         print(f"Patient {jia_patient.name} does not meet criteria for uveitis screening and has been discharged.\n"
    #               f"seek medical assessment urgently if the child develops visual symptoms or signs.\n"
    #               f"These include red eyes, photophobia, abnormal pupils, change in vision or clouding of the eyes.\n"
    #               f"In younger children this may be excess blinking, eye rubbing, visual inattention or a new squint.")


# class JiaPatient(Patient):
#     def __init__(self, name, age, gender, condition_key):
#         super().__init__(self, name, age, gender, condition_key)
#         self.condition_key = 'JIA'
#         self.risk_level = None