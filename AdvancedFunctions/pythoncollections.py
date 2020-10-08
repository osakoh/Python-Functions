"""
- Counter
- defaultdict: never raises a key error
- Orderedict: ordered in the way the elements were inserted
- namedtuple: useful when reading from a file, database etc
- deque: when dealing with threads
All contained in the collections module
"""

from collections import Counter, defaultdict, deque

device_temp = [12, 16, 12, 12, 12.5, 13, 16, 13.5, 14, 14.5, 15, 14, 15.5, 16]

temp_counter = Counter(device_temp)
print(temp_counter)
print(temp_counter[12])

coworkers = [
    ('OS', 'MIT'),
    ('Rolf', 'Oxford'),
    ('OS', 'HARVARD'),
    ('Ann', 'Cambridge'),
]

alma_mater = {}

for person, school in coworkers:
    if person not in alma_mater:
        alma_mater[person] = []
    alma_mater[person].append(school)

# print(alma_mater['Hanna'])  # raises KeyError

alma_mater1 = defaultdict(list)
# alma_mater1.default_factory = None  # to raise a keyError if an element doesn't exist

for person1, school1 in coworkers:
    if person1 not in alma_mater:
        alma_mater[person1].append(school1)

print(alma_mater1['Hanna'])  # doesn't raise KeyError, but returns the default value i.e and empty list

friends = deque(('Ann', 'Charlie', 'Rolf', 'Jen'))
friends.append('Jim')
print(friends)
friends.appendleft('Sue')
print(friends)
friends.pop()
print(friends)
friends.popleft()
print(friends)