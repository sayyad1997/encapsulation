class EMPLOYEE:
    def __init__(self,name,salary,project):
        self.name=name #public modifier
        self.__salary=salary # private modifier
        self._project=project # protected modifier

class DETAILS(EMPLOYEE):
    def __init__(self,name,salary,project):
        super().__init__(name,salary,project)

    def show(self):
        print(f"{self.name} getting salary {self.__salary}")

    def em_details(self):
        print(f"{self.name} working on {self._project}")

details=DETAILS("AFROZ",23000,"NSL")
#calling inside the class
details.em_details()
details.show()

#calling  outside the class
emp=EMPLOYEE("AFROZ",23000,"NSL")
print(emp.name)
print(emp._project)
print(emp.__salary)