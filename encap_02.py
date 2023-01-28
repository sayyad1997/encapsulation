class EMPLOYEE: #base class
    def __init__(self,name,salary):
        #public modifier
        self.name=name
        #protected modifier
        self._salary=salary
        print(f"name of the employee {self.name}, salary of  the employee {self._salary}")


class DETAILS(EMPLOYEE): #derived class
    def __init__(self,name,salary):
        super().__init__(name,salary)

    def em_details(self):
        print(f"name of the employee {self.name}, salary of  the employee {self._salary}")

details=DETAILS("AFROZ",120000)

#calling inside the derived class class
details.em_details()

#calling inside the base class
emp=EMPLOYEE("AFROZ",120000)

#calling outside the class
print(emp.name)
print(details.name)
print(emp._salary)
print(details._salary)