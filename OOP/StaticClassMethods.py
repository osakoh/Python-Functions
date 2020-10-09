class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    # instance method: takes the caller's object(self) as the first parameter
    def average(self):
        return sum(self.marks)/len(self.marks)


std_object = Student('Sau', 'ECE')
std_object.marks.append(89)
std_object.marks.append(90)
# this is an instance method: it takes the caller's object(std_object) as the first parameter
print(std_object.average())  # OR print(Student.average(std_object))


class Foo:
    @classmethod  # takes the class as the first argument
    def hi(cls):
        print("Class method, {} class".format(cls.__name__))


foo_obj = Foo()

# this is a class method: it takes the class as the first parameter
foo_obj.hi()  # OR Foo.hi()


class Bar:
    @staticmethod  # takes nothing as the first parameter
    def hi():
        print("Static method")


bar_obj = Bar()
bar_obj.hi()  # OR Bar.hi()