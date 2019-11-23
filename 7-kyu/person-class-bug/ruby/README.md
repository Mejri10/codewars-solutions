The following code was thought to be working properly, however when the code tries to access the age of the person instance it fails. 

```ruby
person = Person.new('Yukihiro', 'Matsumoto', 47)
puts person.full_name
puts person.age
```
```python
person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name)
print(person.age)
```

For this exercise you need to fix the code so that it works correctly.