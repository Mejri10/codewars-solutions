Something is wrong with our Warrior class. The strike method does not work correctly. The following shows an example of this code being used:

```javascript
var ninja = new Warrior('Ninja');
var samurai = new Warrior('Samurai');

samurai.strike(ninja, 3);
// ninja.health should == 70
```
```typescript
var ninja = new Warrior('Ninja');
var samurai = new Warrior('Samurai');

samurai.strike(ninja, 3);
// ninja.health should == 70
```
```coffeescript
ninja = new Warrior('Ninja')
samurai = new Warrior('Samurai')

samurai.strike(ninja, 3)
# ninja.health should == 70
```
```python
ninja = Warrior('Ninja')
samurai = Warrior('Samurai')

samurai.strike(ninja, 3)
# ninja.health should == 70
```
```ruby
ninja = Warrior.new('Ninja')
samurai = Warrior.new('Samurai')

samurai.strike(ninja, 3)
# ninja.health should == 70
```
```csharp
var ninja = new Warrior("Ninja");
var samurai = new Warrior("Samurai");

samurai.Strike(ninja, 3);
// ninja.Health should == 70
```

Can you figure out what is wrong?
