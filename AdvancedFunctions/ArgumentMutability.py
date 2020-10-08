primes = [2, 3, 5]
print(id(primes))  # both are same because list are mutable

primes += [4, 6, 3]  # this list is being modified. it isn't a new list
print(id(primes))  # both are same because list are mutable


"""
age = 20
print(id(age))


def increase_age(current_age):
    current_age = current_age + 1
    print("inner", id(current_age))  # different from age because integers are immutable


increase_age(age)
print(id(age))
"""

"""
friends_last_seen = {
    'Rolf': 5,
    'Ann': 2,
    'Dave': 3
}
# id is different from Argument id because, integers are immutable
print("outer integer:", id(friends_last_seen['Rolf']))


def see_friends(friends, name):
    print(friends is friends_last_seen)  # checks if both variables are the same object
    friends[name] = 2
    print("Argument dictionary:", id(friends))  # id's same as outer dict because, dictionaries are mutable


print("outer dictionary:", id(friends_last_seen))  # id's same as Argument dict because, dictionaries are mutable
see_friends(friends_last_seen, 'Rolf')
# id is different from outer id because, integers are immutable
print("Argument integer:", id(friends_last_seen['Rolf']))
print(friends_last_seen['Rolf'])
# """
