For a variable, ```x```, that may have different values, ```the geometric mean``` is defined as:

<a href="http://imgur.com/tD9bZui"><img src="http://i.imgur.com/tD9bZui.png" title="source: imgur.com" /></a>

Suposse that you have to calculate **the geometric mean** for a research where the amount of values of x is rather small.

Implement the function ```geometric_meanI()```, (```geometricMeanI javascript```)that receives an array with the different values of the variable and outputs the geometric mean value.

The negative values and strings will be discarded for the calculations. 

Nevertheless if the amount of total invalid values is too high, the function will return ```0``` (Nothing in Haskell). The tolerance for invalid values of the variable will be as follows:

```ruby
amount of entries      maximum invalid entries
  2 - 10                       1
  From 11 and above      < 10 % of total of entries              
```

```javascript
amount of entries      maximum invalid entries
  2 - 10                       1
  From 11 and above       10 % of total of entries              
```

```haskell
amount of entries      maximum invalid entries
  2 - 10                       1
  From 11 and above       10 % of total of entries              
  
```
```python
amount of entries      maximum invalid entries
  2 - 10                       1
  From 11 and above       10 % of total of entries              
```


You do not have to round the results.

(When you finish this kata, Geometric Mean II will be waiting you. http://www.codewars.com/kata/56ec6016a9dfe3346e001242)

