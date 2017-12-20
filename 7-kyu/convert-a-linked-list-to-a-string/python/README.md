# Convert a linked list to a string

## Related Kata

Although this Kata is not part of an official Series, you may also want to try out [Parse a linked list from a string](https://www.codewars.com/kata/582c5382f000e535100001a7) if you enjoyed this Kata.

## Preloaded

Preloaded for you is a class `Node` used to construct linked lists in this Kata:

```php
class Node {
  public $data, $next;
  public function __construct($data, $next = NULL) {
    $this->data = $data;
    $this->next = $next;
  }
}
```
```javascript
class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}
```
```csharp
public class Node {
  public int Data { get; private set; }
  public Node Next { get; private set; }

  public Node(int data, Node next = null) {
    Data = data;
    Next = next;
  }
}
```
```python
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
```
```java
class Node {
	private int data;
	private Node next;
	
	public Node(int data, Node next) {
		this.data = data;
		this.next = next;
	}
	
	public Node(int data) {
		this.data = data;
		this.next = null;
	}

	public int getData() {
		return data;
	}

	public Node getNext() {
		return next;
	}
}
```
```ruby
class Node
  attr_reader :data, :next_node
  
  def initialize(data, next_node=nil)
    @data = data
    @next_node = next_node
  end
end
```
```cpp
class Node
{
  public:
    int data;
    Node* next;
  
  Node(int data, Node* next = nullptr)
  {
    this->data = data;
    this->next = next;
  }
};
```
```haskell
-- You can use regular lists, which are already singly-linked
data [a] = [] | a : [a]
```

## Prerequisites

This Kata assumes that you are already familiar with the idea of a linked list.  If you do not know what that is, you may want to read up on [this article on Wikipedia](https://en.wikipedia.org/wiki/Linked_list).  Specifically, the linked lists this Kata is referring to are **singly linked lists**, where the value of a specific node is stored in its `data`/`$data`/`Data` property, the reference to the next node is stored in its `next`/`$next`/`Next`/`next_node` property and the terminator for a list is `null`/`NULL`/`None`/`nil`.

Additionally, this Kata assumes that you have basic knowledge of Object-Oriented Programming (or a similar concept) in the programming language you are undertaking.  If you have not come across Object-Oriented Programming in your selected language, you may want to try out an online course or read up on some code examples of OOP in your selected language up to (but not necessarily including) Classical Inheritance.

*Specifically, if you are attempting this Kata in PHP and haven't come across OOP, you may want to try out the first 4 Kata in [this Series](https://www.codewars.com/collections/object-oriented-php).*

## Task

Create a function `stringify` which accepts an argument `list`/`$list` and returns a string representation of the list.  The string representation of the list starts with the value of the current `Node`, specified by its `data`/`$data`/`Data` property, followed by a whitespace character, an arow and another whitespace character (`" -> "`), followed by the rest of the list.  The end of the string representation of a list must always end with `null`/`NULL`/`None`/`nil`/`nullptr` (all caps or all lowercase depending on the language you are undertaking this Kata in).  For example, given the following list:

```php
new Node(1, new Node(2, new Node(3)))
```
```javascript
new Node(1, new Node(2, new Node(3)))
```
```csharp
new Node(1, new Node(2, new Node(3)))
```
```python
Node(1, Node(2, Node(3)))
```
```java
new Node(1, new Node(2, new Node(3)))
```
```ruby
Node.new(1, Node.new(2, Node.new(3)))
```
```cpp
new Node(1, new Node(2, new Node(3)))
```
```haskell
[1,2,3]
```

 ... its string representation would be:

```php
"1 -> 2 -> 3 -> NULL"
```
```javascript
"1 -> 2 -> 3 -> null"
```
```csharp
"1 -> 2 -> 3 -> null"
```
```python
"1 -> 2 -> 3 -> None"
```
```java
"1 -> 2 -> 3 -> null"
```
```ruby
"1 -> 2 -> 3 -> nil"
```
```cpp
"1 -> 2 -> 3 -> nullptr"
```
```haskell
"1 -> 2 -> 3 -> null"
```

And given the following linked list:

```php
new Node(0, new Node(1, new Node(4, new Node(9, new Node(16)))))
```
```javascript
new Node(0, new Node(1, new Node(4, new Node(9, new Node(16)))))
```
```csharp
new Node(0, new Node(1, new Node(4, new Node(9, new Node(16)))))
```
```python
Node(0, Node(1, Node(4, Node(9, Node(16)))))
```
```java
new Node(0, new Node(1, new Node(4, new Node(9, new Node(16)))))
```
```ruby
Node.new(0, Node.new(1, Node.new(4, Node.new(9, Node.new(16)))))
```
```cpp
new Node(0, new Node(1, new Node(4, new Node(9, new Node(16)))))
```
```haskell
[0,1,4,6,19]
```

 ... its string representation would be:

```php
"0 -> 1 -> 4 -> 9 -> 16 -> NULL"
```
```javascript
"0 -> 1 -> 4 -> 9 -> 16 -> null"
```
```csharp
"0 -> 1 -> 4 -> 9 -> 16 -> null"
```
```python
"0 -> 1 -> 4 -> 9 -> 16 -> None"
```
```java
"0 -> 1 -> 4 -> 9 -> 16 -> null"
```
```ruby
"0 -> 1 -> 4 -> 9 -> 16 -> nil"
```
```cpp
"0 -> 1 -> 4 -> 9 -> 16 -> nullptr"
```
```haskell
"0 -> 1 -> 4 -> 9 -> 16 -> null"
```

Note that `null`/`NULL`/`None`/`nil`/`nullptr` itself is also considered a valid linked list.  In that case, its string representation would simply be `"null"`/`"NULL"`/`"None"`/`"nil"`/`"nullptr"` (again, depending on the language).

For the simplicity of this Kata, you may assume that any `Node` in this Kata may only contain **non-negative integer** values.  For example, you will not encounter a `Node` whose `data`/`$data`/`Data` property is `"Hello World"`.

Enjoy, and don't forget to check out my other Kata Series :D