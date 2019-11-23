## Preface

A collatz sequence, starting with a positive integer<i>n</i>, is found by repeatedly applying the following function to <i>n</i> until <i>n</i> == 1 :

<img style="margin:auto;display:block;" src="http://latex.codecogs.com/png.latex?\bg_white&space;n&space;=&space;\begin{cases}&space;\frac{n}{2}&space;&&space;\text&space;{if&space;}&space;n&space;\text{&space;is&space;even}&space;\\&space;3n&space;+&space;1&space;&&space;\text{otherwise}&space;\end{cases}" title="collatz sequence" alt="collatz sequence" />

<pre>
 <i>n</i> = { <i>n</i> / 2 for even <i>n</i> ;
      3<i>n</i> + 1 for odd <i>n</i> }
</pre>
=======

A more detailed description of the collatz conjecture may be found [on Wikipedia](http://en.wikipedia.org/wiki/Collatz_conjecture).

## The Problem

Create a function `collatz` that returns a collatz sequence string starting with the positive integer argument passed into the function, in the following form:

"X<sub>0</sub>->X<sub>1</sub>->...->X<sub>N</sub>"

Where X<sub>i</sub> is each iteration of the sequence and N is the length of the sequence.

## Sample Input

```c
collatz(4); // should return "4->2->1"
collatz(3); // should return "3->10->5->16->8->4->2->1"
```
```javascript
collatz(4); // should return "4->2->1"
collatz(3); // should return "3->10->5->16->8->4->2->1"
```
```csharp
Kata.Collatz(4); // should return "4->2->1"
Kata.Collatz(3); // should return "3->10->5->16->8->4->2->1"
```
```ruby
collatz(4) # should return "4->2->1"
collatz(3) # should return "3->10->5->16->8->4->2->1"
```
```python
collatz(4) # should return "4->2->1"
collatz(3) # should return "3->10->5->16->8->4->2->1"
```
```haskell
collatz 2 `shouldBe` "2->1"
collatz 3 `shouldBe` "3->10->5->16->8->4->2->1"
collatz 4 `shouldBe` "4->2->1"
```
```elixir
Collatz.collatz(2) # should return "2->1"
Collatz.collatz(3) # should return "3->10->5->16->8->4->2->1"
Collatz.collatz(4) # should return "4->2->1"
```
```java
Collatz.collatz(2) // should return "2->1"
Collatz.collatz(3) // should return "3->10->5->16->8->4->2->1"
Collatz.collatz(4) // should return "4->2->1"
```

Don't worry about invalid input. Arguments passed into the function are guaranteed to be valid integers >= 1.
