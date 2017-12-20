Given a string (CONTAINS ONLY LETTERS), ``string``, you have to find out the number of unique strings (including ``string`` itself) that can be produced by re-arranging the letters of the ``string``. 

Example: 

``
string = "ABC"
``

``
uniqcount(string) = 6 #=> ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
``

Notes: 
- Find the number of UNIQUE strings!
- Strings are case insensitive. 

HINT: Getting all the uniq strings and calling length on that isn't a great solution for this problem. It can be done a lot faster..

Examples:

``
uniqcount("AB") = 2
``

``
uniqcount("ABC") = 6
``

``
uniqcount("ABA") = 3
``

``
uniqcount("AbcD") = 24
``

``
uniqcount("ABBb") = 4
``
