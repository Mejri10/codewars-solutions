coins = {5: 'Nickels', 1: 'Pennies', 10: 'Dimes', 25: 'Quarters'}

def loose_change(cents):
    purse = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if cents <= 0:
        return purse

    cents = int(cents)
    for value in [25, 10, 5, 1]:
        whole, mod = divmod(cents, value)
        purse[coins[value]] += whole
        cents -= whole * value
    return purse