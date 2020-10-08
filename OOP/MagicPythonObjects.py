"""
Everything in Python is an object. E.g List, Dict, String, Tuple

movies_list = ['one', 'hello']
print(movies_list.__class__)  # <class 'list'>
movies_dict = {'one': 'hello'}
print(movies_dict.__class__)  # <class 'dict'>
movies_string = "one, hello"
print(movies_string.__class__)  # <class 'str'>
movies_tuple = ('one', 'hello')
print(movies_tuple.__class__)  # <class 'tuple'>
"""


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        """
        returns the len of elements in the class
        """
        return len(self.cars)

    def __getitem__(self, index):
        """
        this is a custom function which allows this class to be indexed/sliced.
        Also, the for loop can be used when '__len__ & __getitem__' are implemented in a class
        """
        return self.cars[index]

    def __repr__(self):
        """
        returns a string that represents the class
        used when debugging
        """
        return "<{}>".format(self.cars)

    def __str__(self):
        """
        returns a string information about the garage for the 'user' to read
        """
        return "Garage has {} cars".format(len(self))


ford = Garage()

# new elements can be appended to the Garage class
ford.cars.append('Focus')
ford.cars.append('Explorer')
ford.cars.append('Fiesta')

# print("len: ", len(ford))
# print(ford[::-1])

# for car in ford:
#     print(car)

print(ford)



