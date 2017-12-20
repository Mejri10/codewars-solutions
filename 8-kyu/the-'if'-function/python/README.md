Who likes keywords? Nobody likes keywords, so why use them?

You know what keyword I use too much? `if`! We should __make a function__ called `_if`, with its __arguments as a logical test and two functions/lambdas where the first function is executed if the boolean is true, and the second if it's false__, like an if/else statement, so that we don't have to mess around with those nasty keywords! Even so, __It should support truthy/falsy types__ just like the keyword.


### Example:

```coffeescript
_if(true, (() -> console.log 'true'), (() -> console.log 'false'))
// Logs 'true' to the console.
```
```cpp
void TheTrue() { std::cout << "true" }
void TheFalse() { std::cout << "false" }
_if(true, TheTrue, TheFalse);
// Logs 'true' to the console.
```
``` csharp
Kata.If(true, () => Console.WriteLine("True"), () => Console.WriteLine("False"));
// write "True" to console
```
```elixir
_if(true, fn -> IO.puts "true" end, fn -> IO.puts "false" end)
# prints "true" to the console
```
```haskell
main = _if True (putStrLn "You spoke the truth") (putStrLn "liar")
-- puts "You spoke the truth" to the console.

_if False "Hello" "Goodbye" -- "Goodbye"
```
```javascript
_if(true, function(){console.log("True")}, function(){console.log("false")})
// Logs 'True' to the console.
```
```cpp
void TheTrue() { std::cout << "true" }
void TheFalse() { std::cout << "false" }
_if(true, TheTrue, TheFalse);
// Logs 'true' to the console.
```
```coffeescript
_if(true, (() -> console.log 'true'), (() -> console.log 'false'))
// Logs 'true' to the console.
```
```ruby
_if(true, proc{puts "True"}, proc{puts "False"})
# Logs 'True' to the console.
```
```python
def truthy(): print("True")
def falsey(): print("False")
_if(True, truthy, falsey)
# prints 'True' to the console
```
```ruby
_if(true, proc{puts "True"}, proc{puts "False"})
# Logs 'True' to the console.
```
```elixir
_if(true, fn -> IO.puts "true" end, fn -> IO.puts "false" end)
# prints "true" to the console
```
```rust
_if(true, || println!("true"), || println!("false"))
# prints "true" to the console
```
```lua
kata._if(true, function() print("true") end, function() print("false") end)
-- prints "true" to the console
```
