
import datetime
class Person:




    def __init__(self,first_name,last_name,age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def get_name(self):
        return self._first_name
    def get_name(self):
        return self._last_name
    def get_name(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Age must be large than 0.")

    def display_info(self):
        print(f"Name: {self._first_name},{self._last_name} Age: {self._age}")

class Employee(Person):
    def __init__(self, first_name,last_name,age,employee_start_date):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self.employee_start_date = employee_start_date

        @property
        def start_date(self):
            return self._start_date

        def years_worked(self):
            return datetime.now().year - self.start_date.year

        def offer_pay_rise(self):
            if self.years_worked() >= 5:
                print("Congratulations! You are eligible for a pay rise.")


class Customer(Person):
        def __initi__(self, first_name, last_name, age,date_customer_joined):
            self._first_name = first_name
            self._last_name = last_name
            self._age = age
            self.date_customer_joined = date_customer_joined

            @property
            def start_date(self):
                return self.date_customer_joined

            def years_worked(self):
                return datetime.now().year - self.date_customer_joined

            def offer_discount(self):
                if self.date_customer_joined() >= 5:
                    print("Congratulations! You are eligible for a pay 10% discount.")
    # @employee_start_date.setter
    # def employee_start_date(self,date):



    if __name__ = "__main__":
        person1 =Person("james","brown",30)
        employee = Employee("john","smith",91,datetime(02,10,2019))
        customer1 = Customer("jim","brown",25,datetime(03,04,1994))


class Bankaccount:(Person)
    def __init__(self,first_name,last_name, balance):
        self._first_name = first_name
        self._last_name = last_name
        self.balance = balance
    @property
    def balance(self):
        return self.balance
    def get_name(self):
        return self._first_name

def get_name(self):
    return self._first_name


def get_name(self):
    return self._last_name


def get_name(self):

    def display_info(self):
        print(f"Hello {self.first_name}, your account balance is : {self.balance}")

class Savings(Bankaccount):
    def __init__(self, first_name, last_name, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._balance = balance


class CheckingAccount(Bankaccount):
    def __init__(self, first_name,last_name, balance, overdraft_limit):
        self._first_name = first_name
        self._last_name = last_name
        self._overdraft_limit = overdraft_limit

@property
def overdraft_limit(self):
    return self._overdraft_limit

        def display_info(self):
        super().display_info()
        print(f"hello {self._first_name}this is your Overdraft Limit : {self.overdraft_limit}")
# class Pharmacist(Employee):
#     pass
# pharm_1 = Employee('wendy','williams')
# pharm_2 = Employee('john','smith')
