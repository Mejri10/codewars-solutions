The vowel substrings in the word `codewarriors` are `o,e,a,io`. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only and no spaces, return the length of the longest vowel substring.
Vowels are any of `aeiou`. 

<!-- C# documentation -->
```if:csharp
<h1>Documentation:</h1>
<h2>Kata.Solve Method (String)</h2>

Returns the length of the greatest continuous vowel substring in a string.

<span style="font-size:20px">Syntax</span>
<div style="margin-top:-10px;padding:1px;background-color:Grey;position:relative;left:20px;width:600px;">
  <div style="background-color:White;color:Black;border:1px;display:block;padding:10px;padding-left:18px;font-family:Consolas,Courier,monospace;">
    <span style="color:Blue;">public</span>
    <span style="color:Blue;">static</span>
    <span style="color:Blue;">int</span> Solve(</br>
    <span style="position:relative;left:62px;">string str</span></br>
    )
  </div>
</div>
<div style="position:relative;left:20px;">
  <strong>Parameters</strong>
  </br>
  <i>str</i>
  </br>
  <span style="position:relative;left:50px;">Type: <a href="https://msdn.microsoft.com/en-us/library/system.string(v=vs.110).aspx">System.String</a></span></br>
  <span style="position:relative;left:50px;">The string to be processed.</span>
  </br></br>
  <strong>Return Value</strong>
  </br>
  <span>Type: <a href="https://msdn.microsoft.com/en-us/library/system.int32(v=vs.110).aspx">System.Int32</a></span></br>
  The length of the greatest continuous vowel substring in <i>str</i>, or <strong>0</strong> if <i>str</i> contains no vowels.
</div>
</br></br>
<span style="font-size:20px">Exceptions</span>
</br>
<div style="position:relative;left:20px;">
  <table style="width:350px;border: 1px solid grey;">
    <th style="background-color:#ABABAB;color:#424242;font-weight:bolder;font-size:17px;border: 1px solid grey;">Exception</th>
    <th style="background-color:#ABABAB;color:#424242;font-weight:bolder;font-size:17px;border: 1px solid grey;">Condition</th>
    <tr style="background-color:White;color:Black;">
      <td style="border: 1px solid grey;"><a href="color:https://msdn.microsoft.com/en-us/library/system.argumentnullexception(v=vs.110).aspx" style="color:#3390B1;">ArgumentNullException</a></td>
      <td style="border: 1px solid grey;"><i>str</i> is <b>null</b>.</td>
    </tr>
  </table>
</div>
</br>
```
<!-- end C# documentation -->

Good luck!

If you like substring Katas, please try:

[Non-even substrings](https://www.codewars.com/kata/59da47fa27ee00a8b90000b4)

[Vowel-consonant lexicon](https://www.codewars.com/kata/59cf8bed1a68b75ffb000026)
