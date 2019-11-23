Write a routine that determines the change that should be provided to a user of a vending machine when making a purchase.  The inputs are the price of the item being purchased and the money provided by the user.  The output must be the number and type of coins returned to the user.

The price per item should be greater than $0.00 and not more than money provided to the machine, and that the input money should not be more than $1.00.  

If either of the inputs are outside of this range, return "Invalid input.".  <b><i>Also, the vending machine is currently out of nickels.</i></b>

If the price equals the input money, return "No Change."

Item list:

* Quarter/Quarters=>0.25=>25Pennies
* Dime/Dimes=>0.1=>10Pennies
* Penny/Pennis=>0.01=>1Penny

Example
Given: 0.40, 1.00
Result: 2 Quarters, 1 Dime.