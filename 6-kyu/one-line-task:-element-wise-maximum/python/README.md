# Task

Numpy has a function [numpy.fmax](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.fmax.html) which computes the element-wise maximum for two arrays.

However, there are two problems with this: First, you don't want to get numpy just to use this function. Second, you want a *in-place* version of this function because turning an in-place function into one that creates a new object is trivially easy, but the opposite is not true.

In order to justify your rationale of not using numpy, you want to write the function as short as possible.

The function `fmax`, given arguments `a` and `b`, should compute the element-wise maximum of two arrays, and assign the maximum to `a` *in-place*. The return value of `fmax` is arbitrary as you don't care about it.

# Code Limit

At most `36` characters.
 
# Example

For `a = [1, 2, 3, 4, 5], b = [10, 0, 10, 0, 10]`, `a` should be `[10, 2, 10, 4, 10]` after executing `fmax(a,b)`.

# Input

```
len(a) = len(b)
0 <= len(a), len(b) <= 10000
```

You can guarantee that input arrays only contain integers.