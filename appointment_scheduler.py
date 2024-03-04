
from people.jia_patient import JiaPatient

jia = JiaPatient


class AppointmentScheduler:
    def schedule_next_appointment(self, jia_patient):
        if jia_patient.risk_level == "High" and jia_patient.appointments <= 2 and jia_patient.age <= 11:
            # next_appointment = datetime.now() + timedelta(weeks=8)  # 2 months
            return (f"Next appointment: 8 weeks\n"
                    f"--------------------------------------------------------------------------------------------\n")
        elif jia_patient.risk_level == "High" and jia_patient.appointments > 2 and jia_patient.age <= 11:
            return (f"Next appointment: 16 weeks\n"
                    f"--------------------------------------------------------------------------------------------\n")  # 4 months
        elif jia_patient.risk_level == "High" and jia_patient.appointments <= 2 and jia_patient.age > 11:
            return (f"Next appointment: 8 weeks\n"
                    f"--------------------------------------------------------------------------------------------\n")
        elif jia_patient.risk_level == "High" and jia_patient.appointments < 5 and jia_patient.age > 11:
            return (f"Next appointment: 16 weeks\n"
                    f"--------------------------------------------------------------------------------------------\n")
        else:
            return (f"JIA-related uveitis screening complete. No further appointments have been scheduled.\n"
                    f"--------------------------------------------------------------------------------------------\n")


