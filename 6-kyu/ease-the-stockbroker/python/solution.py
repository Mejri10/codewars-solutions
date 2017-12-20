import re

VALIDATION_REGEX = re.compile(r"\S+ (\d+) (\d*\.\d+) ([BS])")

def parse_order(order):
    quantity, price, status = re.findall(VALIDATION_REGEX, order)[0]
    quantity, price = int(quantity), float(price)
    return (quantity * price, status) 

def balance_statement(lst):
    if not lst:
        return "Buy: 0 Sell: 0"
    orders = lst.split(', ')
    totalBought = totalSold = 0
    invalidOrders = []
    for order in orders:
        if not re.match(VALIDATION_REGEX, order):
            invalidOrders.append(order)
        else:
            total, status = parse_order(order)
            if status == 'B':
                totalBought += total
            else:
                totalSold += total
    if not invalidOrders:
        return "Buy: %d Sell: %d" % (round(totalBought), round(totalSold))
    else:
        return "Buy: %d Sell: %d" % (round(totalBought), round(totalSold)) \
               + "; Badly formed %d: %s ;" % (len(invalidOrders), ' ;'.join(invalidOrders))