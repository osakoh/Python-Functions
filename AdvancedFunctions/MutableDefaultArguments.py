""" -> Mutable default arguments is not a good practice <-
def create_account(name: str, holder: str, account_holders: list = []) -> dict:
    account_holders.append(holder)
    print(id(account_holders))  # both ids are same because it's the same list that is being used (list are mutable)

    return {
        'name': name,
        'main_account_holder': holder,
        'other_account_holders': account_holders
    }


a1 = create_account('savings', 'Pau')
a2 = create_account('current', 'Ann')

print(a2)
"""


# to solve the above problem ^|^
def create_account(name: str, holder: str, account_holders: list = None) -> dict:
    # if account_holders is None:
    if not account_holders:  # if account_holders is None
        account_holders = []

    account_holders.append(holder)
    print(id(account_holders))  # both ids are same because it's the same list that is being used (list are mutable)

    return {
        'name': name,
        'main_account_holder': holder,
        'other_account_holders': account_holders
    }


a1 = create_account('savings', 'Pau')
a2 = create_account('current', 'Ann')

print(a1, "\n", a2)
