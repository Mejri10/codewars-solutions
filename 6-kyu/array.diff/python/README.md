Your goal in this kata is to implement an difference function, which subtracts one list from another.

It should remove all values from list `a`, which are present in list `b`.

```javascript
array_diff([1,2],[1]) == [2]
```
```ruby
array_diff([1,2],[1]) == [2]
```
```python
array_diff([1,2],[1]) == [2]
```
```coffeescript
array_diff([1,2],[1]) == [2]
```
```haskell
difference [1,2] [1] == [2]
```
```csharp
Kata.ArrayDiff(new int[] {1, 2}, new int[] {1}) => new int[] {2}
```


If a value is present in `b`, all of its occurrences must be removed from the other:

```javascript
array_diff([1,2,2,2,3],[2]) == [1,3]
```
```ruby
array_diff([1,2],[1]) == [2]
```
```python
array_diff([1,2,2,2,3],[2]) == [1,3]
```
```coffeescript
array_diff([1,2,2,2,3],[2]) == [1,3]
```
```haskell
difference [1,2,2,2,3] [2] == [1,3]
```
```csharp
Kata.ArrayDiff(new int[] {1, 2, 2, 2, 3}, new int[] {2}) => new int[] {1, 3}
```