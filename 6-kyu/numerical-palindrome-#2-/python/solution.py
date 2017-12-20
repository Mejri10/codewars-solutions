def palindrome(num):
    if not isinstance(num, int):
        return "Not valid"
    elif num < 0:
        return "Not valid"
    else:
        num = str(num)
        for i in range(len(num) - 1):
            for j in range(i+1, len(num)):
                if num[i] == num[j]:
                    p = num[i:j+1]
                    if p == p[::-1]:
                        return True
                    else:
                        break
        return False
            
        