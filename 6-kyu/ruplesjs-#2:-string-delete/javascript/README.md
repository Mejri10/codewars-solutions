You team thanks you for the addition of times for numbers, and because you did such a great job, have asked you to write a delete method for the String object.

## String.delete()

In Ruby, you can delete characters of a string like so:
````
"hello".delete("l") -> "heo"
````

We're going to beef the delete method up a little bit for javascript. 1st, we're going to allow multiple arguments, and we're going to accept strings and regular expressions. String arguments will remove all occurences of the substring. Unlike the string arguments, Regular Expressions must use the global flag to delete all occurences. Invalid arguments should be ignored. Any matches should be removed from the returned string.

Examples:

````javascript
"1: Are you enjoying this kata?".delete(/[^a-z ]/gi) -> " Are you enjoying this kata"
"1: Are you enjoying this kata?".delete("a", "?", [], /[0-9]/g) -> ": Are you enjoying this kt"
````

Enjoy!

<div style="width: 320px; text-align: center; color: white; border: white 1px solid;">
Check out my other RuplesJS katas:
</div>
<div>
<a style='text-decoration:none' href='http://www.codewars.com/kata/ruplesjs-number-1-n-times-do'><span style='color:#00C5CD'>RuplesJS #1:</span> N Times Do</a><br />
<a style='text-decoration:none' href='http://www.codewars.com/kata/ruplesjs-number-2-string-delete'><span style='color:#00C5CD'>RuplesJS #2:</span> String Delete</a><br />
<a style='text-decoration:none' href='http://www.codewars.com/kata/ruplesjs-number-3-string-eachchar'><span style='color:#00C5CD'>RuplesJS #3:</span> String EachChar</a><br />
<a style='text-decoration:none' href='http://www.codewars.com/kata/ruplesjs-number-4-string-formatting'><span style='color:#00C5CD'>RuplesJS #4:</span> String Formatting</a><br />
<a style='text-decoration:none' href='http://www.codewars.com/kata/ruplesjs-number-5-range'><span style='color:#00C5CD'>RuplesJS #5:</span> Range</a><br />
</div>