def alex_mistakes(number_of_katas, time_limit):
    time_left = time_limit - (number_of_katas)*6
    i = total = 0
    while True:
        time_left -= 5 * 2**i
        if time_left < 0:
            break
        else:
            i += 1
    return i
  