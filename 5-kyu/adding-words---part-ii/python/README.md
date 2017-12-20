<p>This is the second part of this kata series. First part is <a href="https://www.codewars.com/kata/adding-words-part-i/">here</a> and the third is <a href="https://www.codewars.com/kata/adding-words-part-iii/">here</a></p>
<p>Add two English words together!</p>
<p>Implement a class <code>Arith</code> such that</p>

```javscript
  var k = new Arith("three");
  k.add("one hundred and two"); //this should return "one hundred and five" 
```

<p><b>Input</b> - Will be between <code>zero</code> and <code>five hundred</code> and will always be in lower case. This input range applies to both the initial value upon object instantiation as well as the input for the <code>add</code> method.</p>
<p><b>Output</b> - Word representation of the result of the addition. Should be in lower case</p>
<p><b>Word format</b> - Both input and output shall be in the format <code>123 = one hundred and twenty three</code>. No hyphen is needed in numbers 21-99. Words should also be separated with one space and no space padding is allowed.