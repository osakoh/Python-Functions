"""
filter(arg1, arg2)
arg1: takes a function that returns True or False
arg2: takes an iterable
filter also returns a generator. So the 'next()' can be called on it
"""


# def starts_with_a(friend):
#     return friend.startswith('A')


friends = ["Rolf", "Ann", "Jen", "Alice", "Alicia"]

# name_a = (filter(starts_with_a, friends))
name_a = (filter(lambda friend: friend.startswith('A'), friends))
name_a_gen = (f for f in friends if f.startswith('A'))  # faster because you don't have to create the lambda function

# print(next(name_a))
# print(next(name_a_gen))


def custom_filter(function, iterable):
    for i in iterable:
        if function(i):  # if function contains i
            yield i


print(custom_filter(name_a, friends))