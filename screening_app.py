# from people.person import Person
# from people.patient import Patient
from people.jia_patient import JiaPatient
from screening_status import ScreeningSchedule
from appointment_scheduler import AppointmentScheduler

# ScreeningSchedule


screening_schedule = ScreeningSchedule()
scheduler = AppointmentScheduler()

# Create JIA patient instances
patient1 = JiaPatient("Peppa Pig", 5, True, 4, 2, 10)
# Add patients to the screening schedule based on risk level
screening_schedule.add_patient(patient1)
print(scheduler.schedule_next_appointment(patient1))
patient2 = JiaPatient("Chloe Pig", 12, False, 6, 5, 5)
screening_schedule.add_patient(patient2)
print(scheduler.schedule_next_appointment(patient2))
patient3 = JiaPatient("Danny Dog", 6, True, 6, 0, 0)
screening_schedule.add_patient(patient3)
print(scheduler.schedule_next_appointment(patient3))



#
# # person_details = JiaPatient(name=(), age=(), gender=())
# # patient = JiaPatient(name=(), age=(), gender=())
# # screening_schedule = ScreeningSchedule()
# # risk_level = Risk(age_of_onset=(), number_of_joints=(), ana_status=())
#
# patient1 = JiaPatient('Ava Smith', 6, 'female', 'JIA')
# print(patient1)
# patient1 = Risk(6, True, 3)
# print(patient1.calculate_risk())
# print(patient1.add_to_screening)