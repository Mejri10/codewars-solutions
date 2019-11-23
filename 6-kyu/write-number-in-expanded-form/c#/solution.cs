using System;
using System.Collections.Generic;

public static class Kata 
{
    public static string ExpandedForm(long num) 
    {
       var expansion = new List<string>();
       while (num > 0)
       {
         var tenthPowerBelow = (long) Math.Pow(10, (long) Math.Log10(num));
         var term = (long) num/tenthPowerBelow*tenthPowerBelow;
         expansion.Add(term.ToString());
         num -= term;
       }
       return string.Join(" + ", expansion);
    }
}