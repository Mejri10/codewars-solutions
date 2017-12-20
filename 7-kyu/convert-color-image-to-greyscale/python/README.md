An array of size N x M represents pixels of an image.
Each cell of this array contains an array of size 3 with the pixel's color information: `[R,G,B]`

Convert the color image, into an *average* greyscale image. 

The `[R,G,B]` array contains integers between 0 and 255 for each color. 

To transform a color pixel into a greyscale pixel, average the values of that pixel:
```js
p = [R,G,B] => [(R+G+B)/3, (R+G+B)/3, (R+G+B)/3]
```

**Note:** the values for the pixel must be integers, therefore you should round floats to the nearest integer.


## Example

Here's an example of a 2x2 image: 
```js
[
 [ [123, 231, 12], [56, 43, 124] ],
 [ [78, 152, 76], [64, 132, 200] ]
]
```
 
Here's the expected image after transformation:
```js
[
 [ [122, 122, 122], [74, 74, 74] ],
 [ [102, 102, 102], [132, 132, 132] ]
]
```


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