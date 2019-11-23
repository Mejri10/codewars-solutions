# Task
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighbouring numbers is equal (note that 0 and n - 1 are neighbouring, too).

 Given `n` and `firstNumber`/`first_number`, find the number which is written in the radially opposite position to firstNumber.

# Example

 For n = 10 and firstNumber = 2, the output should be

```elm
circleOfNumbers n firstNumber == 7
```
```javascript
circleOfNumbers(n, firstNumber) === 7
```
```lua
circleOfNumbers(n, firstNumber) == 7
```
```swift
circleOfNumbers(n, firstNumber) == 7
```
```java
CircleOfNumbers.circleOfNumbers(n, firstNumber) == 7
```
```typescript
circleOfNumbers(n, firstNumber) === 7
```
```shell
run_shell(args: [n, first_number]) == 7
```
```racket
(circle-of-numbers n first-number) ; -> 7
```
```coffeescript
circleOfNumbers(n, firstNumber) is 7
```
```sql
-- run sql with n and first_number => 7
```
```dart
circleOfNumbers(n, firstNumber) == 7
```
```go
circleOfNumbers(n, firstNumber) == 7
```
```elixir
CircleNumbers.circle_of_numbers(n, firstNumber) == 7
```
```factor
n firstNumber circle-of-numbers ! 7
```
```julia
circleofnumbers(n, firstNumber) == 7
```
```r
circle_of_numbers(n, firstNumber) == 7
```
```reason
circleOfNumbers(n, firstNumber) == 7
```
```cpp
circleOfNumbers(n, firstNumber); // --> 7
```
```php
circle_of_numbers($n, $first_number); // -> 7
```
```clojure
(circle-of-numbers n first-number) ; -> 7
```

![](https://codefightsuserpics.s3.amazonaws.com/tasks/circleOfNumbers/img/example.png?_tm=1476003938167)

# Input/Output

 - `[input]` integer `n`

   A positive even integer.

   Constraints: 4 ≤ n ≤ 1000.

 - `[input]` integer `firstNumber`/`first_number`

   Constraints: 0 ≤ firstNumber ≤ n - 1

 - `[output]` an integer
