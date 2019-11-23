Given an array, return the difference between the count of even numbers and the count of odd numbers. `0` will be considered an even number. 

```Haskell
For example:
solve([0,1,2,3]) = 0 because there are two even numbers and two odd numbers. Even - Odd = 2 - 2 = 0.  
```

Let's now add two letters to the last example: 
```Haskell
solve([0,1,2,3,'a','b']) = 0. Again, Even - Odd = 2 - 2 = 0. Ignore letters. 
```

The input will be an array of lowercase letters and numbers only. 

```Haskell
Haskell: 
solve ["0","1","2","3","a","b"] = 0 -- In Haskell, all array elements will be strings.
```
```Python 
Other languages: 
solve([0, 1 ,2, 3, 'a', 'b']) = 0
```

Good luck!

If you like this Kata, please try: 

[Longest vowel chain](https://www.codewars.com/kata/59c5f4e9d751df43cf000035)

[Word values](https://www.codewars.com/kata/598d91785d4ce3ec4f000018)