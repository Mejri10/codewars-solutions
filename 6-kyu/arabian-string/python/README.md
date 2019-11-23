You must create a method that can convert a string from any format into CamelCase. This must support symbols too.

*Don't presume the separators too much or you could be surprised.*

### Tests
```ruby
camelize("example name")   # => ExampleName
camelize("your-NaMe-here") # => YourNameHere
camelize("testing ABC")    # => TestingAbc
```
```python
camelize("example name")   # => ExampleName
camelize("your-NaMe-here") # => YourNameHere
camelize("testing ABC")    # => TestingAbc
```
```javascript
camelize("example name")   // => ExampleName
camelize("your-NaMe-here") // => YourNameHere
camelize("testing ABC")    // => TestingAbc
```