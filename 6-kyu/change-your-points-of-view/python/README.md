We want to define the location `x`, `y` of a `point` on a two-dimensional plane where `x` and `y` are positive integers.

Our definition of such a `point` will return a function (procedure). There are several possible functions to do that.

Possible form of `point`:

```if:racket
~~~
(define (point a b)
  (lambda ...))

(procedure? (point 3 4)) -> #t
~~~
```
```if:python
~~~
def point(a, b):
  return lambda ...

callable(point(3,4)) -> True
~~~
```
```if:javascript
~~~
const point = (a, b) => {
  // your code
};
typeof(point(a, b)) === "function"
~~~
```
```if:scala
~~~
point(a: Int, b: Int): ...  complete ... {
  // your code
};
The type of point(a, b) is "scala.Function..."
~~~
```
```if:fsharp
~~~
point(a: int, b: int): ...  complete ... =
  // your code

The type of point(a, b) is "System.Func..."
~~~
```
```if:csharp
~~~
... complete with the type of your function ... point(int a, int b) {
  // your code
}
The type of point(a, b) is "System.Func..."
~~~
```
```if:vb
~~~
Point(ByVal a As Integer, ByVal b As Integer) As ... complete ...
  ' your code

The type of point(a, b) is "System.Func..."
~~~
```
```if:java
~~~
... complete with the type of your function ... point(int a, int b) {
  // your code
}
The return type of point(a, b) is "java.util.function.Function"
~~~
```

Of course we need to be able to extract from our `point` the two coordinates `x` and `y`.

The function `fst` must return the first element `x` and our function `snd` must return the second element `y`.

We will also write a function `sqr-dist` which returns the square of the distance between two points `point1` and `point2`.

Last function to write `line`:

Given two `points` `foo` and `bar` this function return a list `(l m n)` or `[l, m, n]` where `l, m, n` are the coefficients in 
the general equation `l*x + m*y + n = 0 (1)` of the straight line through the points `foo` and `bar`.

Equation `k*l*x + k*m*y + k*n = 0` is equivalent to (1) and the tests consider that they define the "same" line.

### Examples: See "Sample Tests".

 ```if:racket
 ~~~
 (define foo (point 3 5))
 (procedure? (point 3 5)) -> #t
 (fst foo) -> 3
 (snd foo) -> 5
 (sqr-dist (point 22 55) (point 75 66)) -> 2930
 (line (point 20 22) (point 29 10)) -> '(12 9 -438) ['(4 3 -146) is a good answer too]
 ~~~
```
```if:python
 ~~~
 foo = point(3, 5)
 callable(point(3, 5)) -> True
 fst(foo) -> 3
 snd(foo) -> 5
 sqr-dist(point(22, 55), point(75, 66)) -> 2930
 line(point(20, 22), point(29, 10)) -> [12, 9, -438] ([4, 3, -146] is a good answer too)
 ~~~
```
```if:javascript
 ~~~
 foo = point(3, 5)
 typeof(point(3, 5)) === "function" -> true
 fst(foo) -> 3
 snd(foo) -> 5
 sqr-dist(point(22, 55), point(75, 66)) -> 2930
 line(point(20, 22), point(29, 10)) -> [12, 9, -438] ([4, 3, -146] is a good answer too)
 ~~~
```

## Note:

- Please ask before translating: some translations are already written and published when/if the kata is approved.
