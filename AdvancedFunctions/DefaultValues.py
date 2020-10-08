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


print(add_balance(accounts, 500.90))  # using the default account ('savings')
print(add_balance(accounts, 500, 'checking'))  # overriding the default account
