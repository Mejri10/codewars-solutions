Given two words and a letter, return a single word that's a combination of both words, merged at the point where the given letter first appears in each word. The returned word should have the beginning of the first word and the ending of the second, with the dividing letter in the middle. You can assume both words will contain the dividing letter.

## Examples

```js
StringMerge("hello", "world", "l")       ==>  "held"
StringMerge("coding", "anywhere", "n")   ==>  "codinywhere"
StringMerge("jason", "samson", "s")      ==>  "jasamson"
StringMerge("wonderful", "people", "e")  ==>  "wondeople"
```
```python
string_merge("hello", "world", "l")      ==>  "held"
string_merge("coding", "anywhere", "n")  ==>  "codinywhere"
string_merge("jason", "samson", "s")     ==>  "jasamson"
string_merge("wonderful", "people", "e") ==>  "wondeople"
```
```java
stringMerge("hello", "world", "l")      ==>  "held"
stringMerge("coding", "anywhere", "n")  ==>  "codinywhere"
stringMerge("jason", "samson", "s")     ==>  "jasamson"
stringMerge("wonderful", "people", "e") ==>  "wondeople"
```
```php
stringMerge("hello", "world", "l");      ==>  "held"
stringMerge("coding", "anywhere", "n");  ==>  "codinywhere"
stringMerge("jason", "samson", "s");     ==>  "jasamson"
stringMerge("wonderful", "people", "e"); ==>  "wondeople"
```