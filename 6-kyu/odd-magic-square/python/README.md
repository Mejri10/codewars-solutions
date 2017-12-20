Your task is to create a Magic Square for any positive odd integer n. The Magic Square will contain the integers 1 to the square of n, arranged in an n by n array, such that the columns, rows and both main diagonals add up to the same number. 
<br />The function magicSquare() should return a 2D array as follows:-

### Examples:
```
n=3: Output: [[8,1,6],[3,5,7],[4,9,2]]

8  1  6 
3  5  7 
4  9  2 
```
```
n=5: Output: [[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]]

17  24   1   8  15
23   5   7  14  16
 4   6  13  20  22
10  12  19  21   3
11  18  25   2   9
```

If an even integer is entered the function magicSquare() should return:-
`"Please enter an odd integer."`

For the purposes of this kata start with 1 in the middle of the top row.

**Hint**: Use the <a href="https://en.wikipedia.org/wiki/Siamese_method">De la Loubère or Siamese</a> method of constructing magic squares.


