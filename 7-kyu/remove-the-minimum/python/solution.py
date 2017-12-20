def remove_smallest(numbers):
    if not numbers:
        return []
    else:
        min = numbers[0]
        for number in numbers[1:]:
            if number < min:
                min = number
        numbers.remove(min)        
        return numbers

          
