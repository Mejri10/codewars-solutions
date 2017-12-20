From <a href='https://en.wikipedia.org/wiki/Matryoshka_doll'>Wikipedia</a> : A matryoshka doll (Russian: матрёшка), also known as a Russian nesting doll, or Russian doll, is a set of wooden dolls of decreasing size placed one inside another.

<img src = 'http://www.alkotagifts.com/sites/default/files/styles/gallery_image/public/a03b__61795.jpg?itok=Ax7YjtiI'>

Such dolls are often used for decoration. In this kata, you will be using them to develop your recursion skills.

Your function will receive an instance of class RussianNestingDoll. This russianNestingDoll instance may contain another russianNestingDoll. RussianNestingDolls are callable, such that if a nesting doll contains another nesting doll, calling it [like a function with no parameters, e.g. <code>russianNestingDoll()</code>] will return the smaller nesting doll inside. If it is empty (i.e., it does not contain another doll), it will return <code>None</code>. Your task is to return the size of the smallest doll (russianNestingDolls have a "size" attribute). 

*Don't worry about Python's recursion limit.*  
*Depending on what you value most in your code, you may prefer an iterative solution.*

Happy coding!