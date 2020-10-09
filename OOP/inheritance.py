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

    @property
    def salary_per_week(self):
        """
        returns the weekly salary
        """
        return self.salary * 15

    @property
    def salary_per_month(self):
        """
        returns the monthly salary
        """
        return self.salary_per_week * 4


s = Student('Sau', 'ECE')


s.marks.append(74)
s.marks.append(85)
s.marks.append(90)

print(s.average())

# print(Student.average(s))