<a href="https://imgur.com/Z7HiIU4"><img src="https://i.imgur.com/Z7HiIU4.jpg?1" title="source: imgur.com" /></a>

Cramer (1704 -1752), the swiss mathematician that created a method to solve systems of n linear equations with n variables.

We have a linear system of ```n Equations``` with ```n Variables``` like the following:

<a href="https://imgur.com/IK2keV7"><img src="https://i.imgur.com/IK2keV7.jpg?1" title="source: imgur.com" /></a>

The subindexed values ```a11```, ```a12```, .....```ann```,  are the coefficients of the different variables ```x1```, ```x2```, .....,``` xn```.

We define  ```Δ``` (delta), the determinant of the matrix of the coefficients as it follows:

<a href="https://imgur.com/zvVIYVB"><img src="https://i.imgur.com/zvVIYVB.png?1" title="source: imgur.com" /></a>


You may calculate the determinant also by the way is explained at the kata Matrix Determinant. See at: http://www.codewars.com/kata/matrix-determinant

You may learn also to calculate the determinant: https://en.wikipedia.org/wiki/Determinant

Then, we define the vector, ```V```, with the independent terms ```b1```, ```b2```, ...., ```bn```:

<a href="https://imgur.com/m6m20id"><img src="https://i.imgur.com/m6m20id.png?1" title="source: imgur.com" /></a>

We will obtain the determinants for each variable replacing the vector V for a column in the position of the variable. ```Δx1```, the determinant for the variable ```x1```, ```Δx2```, the determinant for the variable ```x2``` and so on. It is as follows:

<a href="https://imgur.com/GaEIFJV"><img src="https://i.imgur.com/GaEIFJV.png?1" title="source: imgur.com" /></a>

So the values of the variables are:

<a href="https://imgur.com/GMANk3Y"><img src="https://i.imgur.com/GMANk3Y.png?1" title="source: imgur.com" /></a>

We should know that a linear equation system may be solvable, unsolvable or indeterminate as the following chart shows below:

* If Δ ≠ 0 , the equation system is ***solvable***. Each 
  variable will have a value.
  
* If Δ = 0: the system will be ***Unsolvable*** if one of the variables Δx<sub>i</sub> is not 0 or the system will be ***Indeterminate or Unsolvable*** if all the values of Δx<sub>i</sub> are 0.

For that purpose we need a function ```cramer_solver()```, that will accept two arguments, ```matrix``` and ```vector```.


The function will output the array with the following results and order:
```
[Δ, Δx1, Δx2,........,Δxn]
```
But if Δ = 0 and all the Δx<sub>i</sub> are 0, the code will output "Indeterminate or Unsolvable".
If Δ = 0 and at least only one Δx<sub>i</sub> ≠ 0, the code will output "Unsolvable".

If matrix is not square (equal amount of rows and columns) or the lengths of matrix and vector V are different, the code will "Check entries".

Let's see how to solve some example using maths and how the results would be.

We want to solve the following system of equations:
```
4x - 6y - 3z = 12
 x +  y - 2z = 3
4x -20y - 4z = 6
```
So the function will receive the following matrix and vector:

```python
matrix =[[4,-6, -3], [ 1 , 1, -2], [4, -20, -4]]
vector = [12, 3, 6]
cramer_solver(matrix, vector) == [-80, -330, -30, -60]
```

```js
var matrix =[[4,-6, -3], [ 1 , 1, -2], [4, -20, -4]];
var vector = [12, 3, 6];
cramerSolver(matrix, vector) == [-80, -330, -30, -60];
```
Another case:

```
x + y - 3z = -10
x + y - 2z = 3
x + y - 4z = -6
```
So our solver will receive our matrix and vector:
```python
matrix = [[1, 1, -3], [1, 1, -2], [1, 1, -4]]
vector = [-10, 3, -6]
cramer_solver(matrix, vector) == "Unsolvable"
```

```js
var matrix = [[1, 1, -3], [1, 1, -2], [1, 1, -4]];
var vector = [-10, 3, -6];
cramerSolver(matrix, vector) == "Unsolvable"
```
Let's see another more:

```
x + y - 3z = 0
x + y - 2z = 0
x + y - 4z = 0
```

The matrix and vector for this case:

```python
matrix = [[1, 1, -3], [1, 1, -2], [1, 1, -4]]
vector = [0, 0, 0]
cramer_solver(matrix, vector) == "Indeterminate or Unsolvable"
```
```js
var matrix = [[1, 1, -3], [1, 1, -2], [1, 1, -4]];
var vector = [0, 0, 0];
cramerSolver(matrix, vector) == "Indeterminate or Unsolvable"
```

If we introduce a matrix that is not square, the function should detect it.
```python
matrix = [[1, 1, -3, 4], [1, 1, -2, 3], [1, 1, -4, 2]]
vector = [0, 0, 0]
cramer_solver(matrix, vector) == "Check entries"
```
```js
var matrix = [[1, 1, -3, 4], [1, 1, -2, 3], [1, 1, -4, 2]];
var vector = [0, 0, 0];
cramer_solver(matrix, vector) == "Check entries"
```

Also cases where one (or more) row(s) has (have) different lengths.
```python
matrix = [[1, 1, -3], [1, 1], [1, 1, -4]]
vector = [-10, 3, -6]
cramer_solver(matrix, vector) == "Check entries"
```
```js
var matrix = [[1, 1, -3], [1, 1], [1, 1, -4]];
var vector = [-10, 3, -6];
cramerSolver(matrix, vector) == "Check entries"
```

The cases when the dimension of matrix is different than the length of vector should be detected, too.

```python
matrix = [[1, 1, -3, 4], [1, 1, -2, 3], [1, 1, -4, 2], [6, 4, 2, 1]]
vector = [1, 1, 1]
cramer_solver(matrix, vector) == "Check entries"
```
```js
var matrix = [[1, 1, -3, 4], [1, 1, -2, 3], [1, 1, -4, 2], var [6, 4, 2, 1]];
vector = [1, 1, 1];
cramerSolver(matrix, vector) == "Check entries"
```

The coefficients of the equation will be integer values for all the cases, so the array output should have only integers

The tests will challenge your code for linear equations systems up to 8 variables (and 8 equations obviously)

Enjoy it!!

(Javascript and Ruby versions will be released soon)