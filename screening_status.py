from people.jia_patient import JiaPatient

jia = JiaPatient


class ScreeningSchedule:
    def __init__(self):
        self.patients_for_screening = []

    def add_patient(self, jia_patient):
        if jia_patient.risk_level == "High":
            self.patients_for_screening.append(jia_patient)
            print(f"--------------------------------------------------------------------------------------------\n"
                  f"{jia_patient.name}\n"
                  f"Age: {jia_patient.age} years\n"
                  f"JIA-related uveitis risk level = HIGH\n"
                  f"The child is eligible for uveitis screening.\n"
                  f"Screen every 2 months for 6 months. Then screen every 4 months until the child turns 12.\n"
                  f"--------------------------------------------------------------------------------------------")
        else:
            print(f"--------------------------------------------------------------------------------------------\n"
                  f"{jia_patient.name}\n"
                  f"Age: {jia_patient.age} years\n"
                  f"JIA-related uveitis risk level = LOW\n"
                  f"The child does not meet criteria for uveitis screening and has been discharged.\n"
                  f"Advise parents to seek medical assessment urgently if the child develops visual symptoms or signs.\n"
                  f"These include red eyes, photophobia, abnormal pupils, change in vision or clouding of the eyes.\n"
                  f"In younger children this may be excess blinking, eye rubbing, visual inattention or a new squint.\n"
                  f"--------------------------------------------------------------------------------------------")
