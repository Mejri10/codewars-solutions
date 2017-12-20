In this Kata, we use the Euler method for integrating a function (see [wiki](https://en.wikipedia.org/wiki/Euler_method)).

Remember that integrating a function basically means 'calculating the area under a curve'. One way to approximate the area is to chop it up into rectangles (whose area is just height * width) and sum them (see [this other wiki page](https://en.wikipedia.org/wiki/Rectangle_method) which has a nice gif illustrating this point). We are going to do just this.

Let  `y = 5 + 2 * x + 3 * x^2`. 

Write a function 

```def euler(stop, step_size)```

that calculates the integral of y between `x = 0` and `x = stop`.  For the sake of simplicity, `stop > 0`.

As the example test shows, the code will be verified by using a `step_size of 0.0001`, then rounding the output to the nearest integer. 