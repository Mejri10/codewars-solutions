My washing machine uses ```L``` amount of water to wash ```X``` amount of clothes.  For every 1 unit increase in clothes, the washing machine will use 10% more water to clean (i.e. ```For X = X + 1, L = L * 110%```.

Write a function ```howMuchWater``` (JS)/```how_much_water``` (Python) to work out how much water is needed if you have a ```N``` amount of clothes.  The function will accept 3 parameters - ```howMuchWater(L, X, N)``` / ```how_much_water(L,X,N)```

My washing machine is an old model that can only handle double the amount of ```X```.  If ```N > 2X```, return ```'Too much clothes'```.  The washing machine also cannot handle any amount of clothes less than ```X```.  If that is the case, return ```'Not enough clothes'```.

The answer should be rounded to the nearest 2 decimal places.
