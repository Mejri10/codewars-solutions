Ore Numbers (Also called Harmonic Divisor Numbers) are numbers for which the harmonic mean (https://en.wikipedia.org/wiki/Harmonic_mean) of all their divisors (including the number itself) equals an integer.

For example, 6 is an Ore Number because its harmonic mean is exactly 2.

```harmonic_mean(6) = 4/(1/1+1/2+1/3+1/6) = 2```

Your task is to write a function ```isOre(n)``` that returns ```True``` (**JS** `true`) if n is an Ore Number and ```False``` (**JS** `false`) otherwise.

(Hint: The harmonic mean is the total number of divisors divided by the sum of their reciprocals.)

You can assume all inputs will be valid positive integers.