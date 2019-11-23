using System;
using System.Linq;
using System.Collections.Generic;

public static class Kata
{
  public static string GenerateShape(int n)
  {
    return string.Join(
      "\n",
      Enumerable
        .Range(0, n)
        .Aggregate(new List<string>(n), (lst, _) => {
            lst.Add(new string('+', n));
            return lst;
        })
    );
  }
}