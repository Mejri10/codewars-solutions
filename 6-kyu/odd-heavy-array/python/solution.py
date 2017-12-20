def isOddHeavy(arr):
    """
    Time complexity: O(N) whereby N is length arr.
    """
    greatestEvenNumber = float("-inf")
    lowestOddNumber = float("inf")
    for n in arr:    
        if n % 2 == 0:
            if n > greatestEvenNumber:
                greatestEvenNumber = n
        else:
            if n < lowestOddNumber:
                lowestOddNumber = n    
        if lowestOddNumber < greatestEvenNumber:
            return False            
    return lowestOddNumber != float('inf')