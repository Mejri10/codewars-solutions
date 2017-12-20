def solve(arr):
    arrSorted = sorted(arr, reverse=True)
    answer = []
    n = len(arrSorted)
    for i in range(n//2):
        answer.append(arrSorted[i])
        answer.append(arrSorted[n - i - 1])
    return answer if n % 2 == 0 else answer + [arrSorted[n//2]]