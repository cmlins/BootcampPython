class Employee:
    'Common base for all employess'
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print(f'employee counter: {emp_count}')

    def display_employee (self):
        print(f'name: {self.name}, salary: {self.salary}')


empregado1 = Employee('Cinthya', 987452348957)
print(empregado1.name)