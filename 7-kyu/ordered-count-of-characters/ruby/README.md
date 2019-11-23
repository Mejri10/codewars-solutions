Count the number of occurrences of each character and return it as a list of tuples in order of appearance.

Example:
```python
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
```

```ruby
ordered_count("abracadabra") == [['a', 5], ['b', 2], ['r', 2], ['c', 1], ['d', 1]]
```

```haskell
orderedCount "abracadabra" == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
```

```scala
Kata.orderedCount("abracadabra") == List(('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1))
```

```groovy
Kata.orderedCount("abracadabra") == [['a', 5], ['b', 2], ['r', 2], ['c', 1], ['d', 1]]
```

```csharp
Kata.orderedCount("abracadabra") == new List<Tuple<char, int>> () { new Tuple<char, int>('a', 5), new Tuple<char, int>('b', 2), new Tuple<char, int>('r', 2), new Tuple<char, int>('c', 1), new Tuple<char, int>('d', 1)}
```

```javascript
orderedCount("abracadabra") == [['a', 5], ['b', 2], ['r', 2], ['c', 1], ['d', 1]]
```

```julia
# Note the single quotes: don't use a string, a character is used instead
orderedCount("abracadabra") == [['a', 5], ['b', 2], ['r', 2], ['c', 1], ['d', 1]]
```
```crystal
# Note the single quotes: don't use a string, a character is used instead
ordered_count("abracadabra") == [{'a', 5}, {'b', 2}, {'r', 2}, {'c', 1}, {'d', 1}]
```

```php
orderedCount("abracadabra") == [['a', 5], ['b', 2], ['r', 2], ['c', 1], ['d', 1]]
```

```fsharp
orderedCount("abracadabra") = [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
```

```c
ordered_count("abracadabra", *szout);

// using:
typedef struct Character_Count_Pair {
    char character;
    size_t count;
} ccp;

// returns:
{{'a', 5}, {'b', 2}, {'r', 2}, {'c', 1}, {'d', 1}}

// assigns length:
szout = 5

```