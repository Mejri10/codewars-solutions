You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

Your function will accept three arguments:<br>
The first and second argument will be numbers.<br>
The third argument will represent a sign indicating the operation to perform on these two numbers.

# Example:

```javascript
calculator(1,2,"+"); //=> result will be 3
```
```php
calculator(1, 2, "+"); // 3
```
```csharp
Kata.Calculator(1, 2, '+') => 3
```
```python
calculator(1, 2, '+') => 3
```

```if-not:csharp
if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.
```
```if:csharp
If the sign is not a valid sign, throw an ArgumentException.
```

# Example:

```javascript
calculator(1,2,"&"); //=> result will be "unknown value"
calculator(1,"k","*"); //=> result will be "unknown value"
```
```php
calculator(1, 2, "&"); // "unknown value"
calculator(1, "k", "*"); // "unknown value"
```
```csharp
Kata.Calculator(1, 2, '$') // throws ArgumentException
```
```python
calculator(1, 2, '$') # result will be "unknown value"
```

Good luck!