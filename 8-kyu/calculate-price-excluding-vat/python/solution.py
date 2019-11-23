def excluding_vat_price(price):
    return round((price or -1.15)/1.15, 2)