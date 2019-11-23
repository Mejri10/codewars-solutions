Implement a function named generateRange(min, max, step), which takes three arguments and generates a range of integers from min to max, with the step. The first integer is the minimum value, the second is the maximum of the range and the third is the step. (min < max)

### Task
Implement a function named

```javascript
generateRange(2, 10, 2) // should return array of [2,4,6,8,10]
generateRange(1, 10, 3) // should return array of [1,4,7,10]
```
```elixir
generate_range(2, 10, 2) # should return array of [2,4,6,8,10]
generate_range(1, 10, 3) # should return array of [1,4,7,10]
```
```csharp
GenerateRange(2, 10, 2) == new int[]{ 2, 4, 6, 8, 10 }
GenerateRange(1, 10, 3) == new int[]{ 1, 4, 7, 10 }
```
```racket
(generate-range 2 10 2) ; '(2 4 6 8 10)
(generate-range 1 10 3) ; '(1 4 7 10)
```

### Note
- min < max
- step > 0
- the range does not HAVE to include max (depending on the step)

