Given a string, write a function that returns the string with a question mark ("?") appends to the end, unless the original string ends with a question mark, in which case, returns the original string.

```elixir
ensure_question("Yes") == "Yes?" 
ensure_question("No?") == "No?"
```
```ruby
ensure_question("Yes") # => "Yes?" 
ensure_question("No?") # => "No?"
```