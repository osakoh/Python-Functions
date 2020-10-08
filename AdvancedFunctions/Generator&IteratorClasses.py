class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):  # makes this function an iterator. allows you to call next(object)
        if self.number < 100:
            current = self.number
            print("before self.number->", self.number)
            print("before current->", current)
            self.number += 1
            print("after self.number->", self.number)
            print("after current->", current)
            return current  # current = 0
        else:
            raise StopIteration  # tells Python to stop the iteration


# my_gen = FirstHundredGenerator()
# print(next(my_gen), '\n')
# print(next(my_gen), '\n')


# Iterables are objects with the __iter__ method. They can be it
class FirstHundredIterable:
    def __iter__(self):  # makes this function an iterable
        return FirstHundredGenerator()


# print(sum(FirstHundredIterable()))

# this is Generator comprehension not tuple comprehension
my_num_gen = (x for x in range(10))
print(next(my_num_gen))


# not all iterators are generators, but all generators are iterators(has the __next__())

# class FirstFiveIterator:
#     def __init__(self):
#         self.numbers = [1, 2, 3, 4, 5]
#         self.i = 0
#
#     def __next__(self):
#         if self.i < len(self.numbers):
#             current = self.numbers[self.i]
#             self.i += 1
#             return current
#
#
# my_it = FirstFiveIterator()
# print(next(my_it))
# print(next(my_it))


