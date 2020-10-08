accounts = {
    'checking': 2000.58,
    'savings': 5500.50
}


def add_balance(dict_name: dict, amount: float, acc_type: str = 'savings') -> float:
    """
    function to update the balance of an account
    returns a new balance
    default values must be at the end
    """
    dict_name[acc_type] += amount
    return dict_name[acc_type]


transactions = [
    (accounts, -180.84),
    (accounts, -160.04, 'checking'),
    (accounts, 500.00, 'checking'),
    (accounts, -900.50, 'savings'),
    (accounts, 125.84, 'checking')
]

for t in transactions:
    # add_balance(t[0], t[1])
    add_balance(amount=t[1], dict_name=t[0])  # an adv of using named parameters is that they can be put in any order
    # add_balance(*t)  # argument unpacking. The *(asterisk) is the unpacking operator

print(accounts)


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

# user_objects = [User(password=data['password'], username=data['username']) for data in users]
user_objects = [User(**data) for data in users]
print(user_objects)

