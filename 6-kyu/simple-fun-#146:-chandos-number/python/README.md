# Task
 The sequence of `Chando` is an infinite sequence of all Chando's numbers in ascending order.

 A number is called `Chando's` if it is an integer that can be represented as a sum of different positive integer powers of 5.

 The first Chando's numbers is 5 (5^1). And the following n<sup>th</sup> Chando's numbers are:
 ```
 25  (5^2)
 30  (5^1 + 5^2)
 125 (5^3)
 130 (5^1 + 5^3)
 150 (5^2 + 5^3)
 ...
 ...
 ```

 Your task is to find the Chando's n<sup>th</sup> number for a given `n`.

# Input/Output


 - `[input]` integer `n`

  `1 <= n <= 7000`


 - `[output]` an integer

  n<sup>th</sup> Chando's number