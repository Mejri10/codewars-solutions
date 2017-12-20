The objective of '<a href="https://en.wikipedia.org/wiki/Duck,_duck,_goose">Duck, duck, goose</a>' is to <u>walk in a circle</u>, tapping on each player's head until one is finally chosen.
<br>

<span style="border: 5px solid black; 150%;background-color:black;"><span style="color:red; font-size: 1.25em"><b><u>Task</u></b></span>:
Given an array of Player objects (an array of associative arrays in PHP) and an index (**1-based**), return the name of the chosen Player.</span>
<br>

Example:
<div style="border: 1px solid grey; background-color: black">
`duck_duck_goose([a, b, c, d], 1) should return a.name`
`duck_duck_goose([a, b, c, d], 5) should return a.name`
`duck_duck_goose([a, b, c, d], 4) should return d.name`
</div>

```php
// PHP only
duck_duck_goose([$a, $b, $c, $d], 1); // => $a["name"]
duck_duck_goose([$a, $b, $c, $d], 5); // => $a["name"]
duck_duck_goose([$a, $b, $c, $d], 4); // => $d["name"]
```