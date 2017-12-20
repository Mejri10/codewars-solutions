def bmi(w, h):
    index = w/h**2
    if index <=  18.5:
        msg = "Underweight"
    elif index <= 25:
        msg = "Normal"
    elif index <= 30:
        msg = "Overweight"
    else:
        msg = "Obese"    
    return msg