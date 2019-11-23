using System;
using System.Collections.Generic;
using System.Linq;

public static class Kata
{
  public static List<int> MultipleOfIndex(List<int> xs)
  {
    return xs.Where((n, idx) => idx == 0 ? false : n % idx == 0).ToList();
  }
}