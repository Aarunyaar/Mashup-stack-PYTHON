class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")


class PartTime(Person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours = working_hours

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")


class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name

    def show_details(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, "
            f"Working Hours: {self.working_hours}, Project: {self.project_name}"
        )


p1 = Person("Alice", 30)
e1 = Employee("Bob", 28, "EMP101")
pt1 = PartTime("Charlie", 22, 4.5)
c1 = Consultant("David", 35, "CONS202", 6, "AI System")

p1.show_details()
e1.show_details()
pt1.show_details()
c1.show_details()
