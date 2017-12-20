An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: Exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP.  Find the missing term.  

You have to write the function findMissing (list) , list will always be atleast 3 numbers. The missing term will never be the first or last one.

Example:

```php
findMissing([1,3,5,9,11]) == 7
```
```objc
findMissing(@[@1, @3, @5, @9, @11]); // => @7
```
```csharp
Kata.FindMissing(new List<int> {1, 3, 5, 9, 11}) => 7
```

PS: This is a sample question of the facebook engeneer challange on interviewstreet.
I found it quite fun to solve on paper using math , derive the algo that way.
Have fun!

~~~if:objc
### Objective-C Specific Notes

The list of numbers `list` passed into your function will be passed in as (a pointer to) an `NSArray` of `NSNumber`s.  Furthermore, you should return your result as (a pointer to) an `NSNumber`.  You may assume that all numbers involved will not exceed the range of a 32-bit signed integer.
~~~