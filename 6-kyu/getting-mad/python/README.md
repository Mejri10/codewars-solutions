<h2>Getting the Minimum Absolute Difference</h2>

<h2>Task</h2>

Given an array `arr = a1,a2,a3,a4, ... aN` and consider the absolute difference between two elements as the absolute value of `ai - aj`, where `i != j` for any elements in `arr`. 

Find the minimum absolute difference (MAD) between any two elements in `arr`.

<h2>Example</h2>

For `arr = [-10,0,-3,1]`

The MAD is `1`.
<h2>Explanation:</h2>
```
|0-10| = 10
|-3-(-10)| = 7
|1-10| = 9
|-10-0| = 10
|-3-0| = 3
|1-0| = 1
|-10-(-3)| = 7
|0-3| = 3
|1-3| = 2
|-10-(-3)| = 7
|0-3| = 3
|1-3| = 2
|-10-1)| = 11
|0-1| = 1
|-3-1| = 4
```
The minimum value is `1`.


Note that the same value can appear more than once in `arr`. In that case, the MAD will be `0`.

Also, each array has at least two elements and its contains only integers. You can consider the `arr` as a valid one and do not need to validate it.