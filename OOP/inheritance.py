class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)  # calls Student __init__()
        self.salary = salary

    def salary_per_week(self):
        return self.salary * 15

    def salary_per_month(self):
        return self.salary_per_week() * 4


sau = WorkingStudent('Sau', 'ECE', 12.50)
print(sau.salary)
print(sau.salary_per_week())
print(sau.salary_per_month())

sau.marks.append(74)
sau.marks.append(85)
sau.marks.append(90)

print(sau.average())