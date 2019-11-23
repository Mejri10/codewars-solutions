using System;
using System.Collections.Generic;
using System.Linq;

public static class Kata
{
  public static IEnumerable<string> MyLanguages(Dictionary<string, int> results)
  {
    return (IEnumerable<string>) results.Where(entry => entry.Value >= 60)
      .OrderByDescending(entry => entry.Value)
      .Select(entry => entry.Key);
  }
}