def lose_weight(gender, weight, duration):
    if gender != "M" and gender != "F": return "Invalid gender"
    if weight <= 0: return "Invalid weight"
    if duration <= 0: return "Invalid duration"
    
    return round(weight * (1 - [1.5/100, 1.2/100][gender=='F']) ** duration, 1)