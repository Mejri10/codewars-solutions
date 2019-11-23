def solution(digits):
    largest = 0
    for i in range(len(digits) - 4):
        current_val = int(digits[i: i+5]) 
        if current_val > largest:
            largest = current_val
    return largest