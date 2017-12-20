Ahoy matey!

You are a leader of a small pirate crew. And you have a plan.
With the help of OOP you wish to make a pretty eficient system to identify ships with a heavy booty on board. 

Unfortunattely for you, people weigh a lot this days, so how do you know if a ship if full of gold and not people?

You begin with writing a generic Ship class:
```javascript
function Ship(draft,crew) {
 this.draft = draft;
 this.crew = crew;
}
```
```python
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
```
```csharp
public class Ship
{
  public int Draft;
  public int Crew;
  
  public Ship(int draft, int crew)
  {
    Draft = draft;
    Crew = crew;
  }
}
```
Every time your spies see a new ship enter the dock, they will create a new ship object:
```javascript
var titanic = new Ship(15,10);
```
```python
Titanic = Ship(15,10)
```
```csharp
Ship titanic = new Ship(15, 10);
```

Now comes the tricky part:
An average man will sink the ship by exactly `1.5` units. (Ship's draft goes up)
That means the draft can show the estimated weight of the presumable booty aboard.

if it weighs more than `20` without people, it is worthy to board.
Your system should have a method
```javascript
isWorthIt
``` 
```python
is_worth_it
``` 
```csharp
IsWorthIt
```
to decide that:

```javascript
titanic.isWorthIt() //return false
```
```python
Titanic.is_worth_it() #return false
```
```csharp
titanic.IsWorthIt() => false
```
This Kata teaches you the very basic of method creation.

Good luck!
