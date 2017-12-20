Implement a function ```kPermutationsOfN``` that accepts a list of elements ```indices``` and an integer ```k```, and returns all permutations of elements from the list ```indices```. Permutations should be a list containing all unique lists of ```k``` elements from ```indices```.

For example, if ```indices==[1,2,3]``` and ```k==2``` the result should be: 
```python
[[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
```

If ```indices``` is an empty list or if ```k>len(indices)``` the function should return a list containing an empty list, i.e.```[[]]```. Also, if ```indices``` is a non-empty list and ```k==0```, the function should return ```[[]]```.

You can assume that the input list ```indices``` contains unique elements.