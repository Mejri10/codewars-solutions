Write a function that accepts two parameters (a and b) and says whether a is smaller than, bigger than, or equal to b.

Here is an example code:
<pre><code>var noIfsNoButs = function (a,b) {
  if(a > b) return a + " is greater than " + b
  else if(a < b) return a + " is smaller than " + b
  else if(a == b) return a + " is equal to " + b
}
</code></pre>

There's only one problem...

You can't use if statements, and you can't use shorthands like <code>(a < b)?true:false;</code>

in fact the word "if" and the character "?" are not allowed in the code. 


<b>Inputs are guarenteed to be numbers</b>


<center>
You are always welcome to check out some of my other katas:

<b>Very Easy (Kyu 8)</b>

<a href="https://www.codewars.com/kata/5926d7494b2b1843780001e6">Add Numbers</a>

<b>Easy (Kyu 7-6)</b>

<a href="https://www.codewars.com/kata/590ee3c979ae8923bf00095b">Convert Color image to greyscale</a><br>
<a href="https://www.codewars.com/kata/591190fb6a57682bed00014d">Array Transformations</a><br>
<a href="https://www.codewars.com/kata/5914e068f05d9a011e000054">Basic Compression</a><br>
<a href="https://www.codewars.com/kata/5927db23fb1f934238000015">Find Primes in Range</a><br>
<a href="https://www.codewars.com/kata/592915cc1fad49252f000006">No Ifs No Buts</a>

<b>Medium (Kyu 5-4)</b>

<a href="https://www.codewars.com/kata/5910b92d2bcb5d98f8000001">Identify Frames In An Image</a><br>
<a href="https://www.codewars.com/kata/5912950fe5bc241f9b0000af">Photoshop Like - Magic Wand</a><br>
<a href="https://www.codewars.com/kata/59255740ca72049e760000cd">Scientific Notation</a><br>
<a href="https://www.codewars.com/kata/59267e389b424dcd3f0000c9">Vending Machine - FSA</a><br>
<a href="https://www.codewars.com/kata/59293c2cfafd38975600002d">Find Matching Parenthesis</a>

<b>Hard (Kyu 3-2)</b>

<a href="https://www.codewars.com/kata/59276216356e51478900005b">Ascii Art Generator</a>