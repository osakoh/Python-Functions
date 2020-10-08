"""
-map(fun, iter) function returns a map object(which is an iterator) of the results after applying
the given function to each item of a given iterable (list, tuple etc.)
-map function also returns a generator
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.
"""

friends = ["Rolf", "Ann", "Jen", "Alice", "Alicia"]

# name_a = (filter(starts_with_a, friends))
name_a = (filter(lambda friend: friend.startswith('A'), friends))

friends_lower = map(lambda friend: friend.lower(), friends)
# friends_lower = [friend.lower() for friend in friends]
# friends_lower = (friend.lower() for friend in friends)

print(next(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dictionary(cls, data):
        return cls(data['username'], data['password'])


users = [
    {'username': 'ann', 'password': '124'},
    {'username': 'rolf', 'password': '345'}
]

# show_user_data = [User.from_dictionary(user)for user in users]
show_user_data = map(User.from_dictionary, users)
print(show_user_data)