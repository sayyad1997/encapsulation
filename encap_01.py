class EMPLOYEE:
    def __init__(self,name,salary,project):
        #public modifier
        self.name=name
        self.salary=salary
        self.project=project

    def show(self):
        print(self.name, "getting salary ", self.salary)

    def work (self):
        print(self.name , "working on ", self.project)

employee=EMPLOYEE("AFROZ",12000,"NSL")

#calling inside the class
employee.show()
employee.work()

#calling outside the class 
print(employee.name, "getting salary ", employee.salary)
print(employee.name , "working on ", employee.project)

#NOTE:- pubplic modifier we can call from inside and out side the class

employee.name