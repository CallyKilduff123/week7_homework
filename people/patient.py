from people.person import Person


class Patient(Person):
    def __init__(self, name, age, condition):
        super().__init__(name, age)
        self.condition = condition

    # def ensure_paediatric_patient(self):
    #     if self.age >= 16:
    #         return f"Adult patient: Not eligible for paediatric services."
    #     else:
    #         return f"Paediatric patient"
    #
    # def define_condition(self):
    #     if self.condition == 'JIA':
    #         return (f"-------------------------------------------\n"
    #                 f"JIA patient: Follow JIA Screening Protocol\n"
    #                 f"-------------------------------------------\n")




# class Patient(Person):
#
#     def __init__(self, name, age, gender, condition_key):
#         super().__init__(name, age, gender)
#         self.condition_key = condition_key
#
#         self.condition = {
#             'JIA': 'Juvenile Idiopathic Arthritis',
#             'AAU': 'Acute Anterior Uveitis',
#             'PU': 'Posterior/Intermediate Uveitis'}
#
#         self.condition.get(self.condition_key)

    # def __str__(self):
    #     uveitis = self.condition.get(self.condition_key)
    #     return f"Condition: {uveitis}"



    # def get_age_related_condition(self, age, condition):
    #     if age >= 16:
    #         return "consider Acute Anterior Uveitis"
    #     elif age >= 8:
    #         return "consider Posterior or intermediate uveitis"
    #     else:
    #         return "consider Juvenile Idiopathic Arthritis with uveitis"
#
# if __name__ == "__main__":



