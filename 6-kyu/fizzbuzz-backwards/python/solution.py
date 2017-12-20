def reverse_fizz_buzz(array):
    if "Fizz" in array and "Buzz" in array:
        return array.index("Fizz") + 1, array.index("Buzz") + 1
    elif "Fizz" in array and "FizzBuzz" in array:
        return array.index("Fizz") + 1, array.index("FizzBuzz") + 1
    elif "Buzz" in array and "FizzBuzz" in array:
        return array.index("FizzBuzz") + 1, array.index("Buzz") + 1
    elif "Fizz" not in array and "Buzz" not in array and "FizzBuzz" in array:
        return array.index("FizzBuzz") + 1, array.index("FizzBuzz") + 1
    else:
        return []