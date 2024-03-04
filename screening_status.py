from people.jia_patient import JiaPatient

jia = JiaPatient


class ScreeningSchedule:
    def __init__(self):
        self.patients_for_screening = []

    def add_patient(self, jia_patient):
        if jia_patient.age >= 16:
            return (f"--------------------------------------------------------------------------------------------\n"
                    f"{jia_patient.name}\n"
                    f"Age: {jia_patient.age} years\n"
                    f"Adult patient - not eligible for paediatric services\n"
                    f"--------------------------------------------------------------------------------------------")
        elif jia_patient.risk_level == "High":
            self.patients_for_screening.append(jia_patient)
            return (f"--------------------------------------------------------------------------------------------\n"
                    f"{jia_patient.name}\n"
                    f"Age: {jia_patient.age} years\n"
                    f"JIA-related uveitis risk level = HIGH\n"
                    f"The child is eligible for uveitis screening.\n"
                    f"Screen every 2 months for 6 months. Then screen every 4 months until the child turns 12.\n"
                    f"--------------------------------------------------------------------------------------------")
        else:
            return (f"--------------------------------------------------------------------------------------------\n"
                    f"{jia_patient.name}\n"
                    f"Age: {jia_patient.age} years\n"
                    f"JIA-related uveitis risk level = LOW\n"
                    f"The child does not meet criteria for uveitis screening and has been discharged.\n"
                    f"Advise parents to seek medical assessment urgently if the child develops visual symptoms or signs.\n"
                    f"These include red eyes, photophobia, abnormal pupils, change in vision or clouding of the eyes.\n"
                    f"In younger children this may be excess blinking, eye rubbing, visual inattention or a new squint.\n"
                    f"--------------------------------------------------------------------------------------------")

    # def get_screening_list(self):
    #     return patients_for_screening

    # def get_screening_list(self):
    #     if not self.patients_for_screening:
    #         return "No patients are currently scheduled for screening."
    #
    #     patient_details = ["Patients scheduled for JIA uveitis screening:"]
    #     for patient in self.patients_for_screening:
    #         detail = f"Name: {patient.name}, Age: {patient.age}, Condition: {patient.condition}"
    #         patient_details.append(detail)
    #
    #     return "\n".join(patient_details)  # Returns a single string