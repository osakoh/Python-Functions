"""
any(): Returns true if any of the items is True. It returns False if empty or all are false.
Any can be thought of as a sequence of OR operations on the provided iterables.
It short circuit the execution i.e. stop the execution as soon as the result is known.
Syntax : any(list of iterables)

all(): Returns true if all of the items are True (or if the iterable is empty).
All can be thought of as a sequence of AND operations on the provided iterables.
It also short circuit the execution i.e. stop the execution as soon as the result is known.

Syntax : all(list of iterables)
"""

friends = [
    {
        'name': 'Jose',
        'location': 'SA'
    },
    {
        'name': 'Ann',
        'location': 'NG'
    },
    {
        'name': 'Rolf',
        'location': 'NG'
    }
]

your_location = input("Enter your location? ").upper()
friends_nearby = [friend for friend in friends if friend['location'] == your_location]
# print(friends_nearby)

if all(friends_nearby):  # Returns True if there's at least one; or False if empty
    print(friends_nearby)
