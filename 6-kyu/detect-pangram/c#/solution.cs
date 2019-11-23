using System;
using System.Collections.Generic;
using System.Linq;

public static class Kata
{
  private static string ALPHABET = "abcdefghijklmnopqrstuvwxyz";
  
  public static bool IsPangram(string str)
  {
    var freqs = charFreq(str.ToLower());
    return ALPHABET.All(c => freqs.ContainsKey(c) && freqs[c] >= 1);
  }
  
  private static IDictionary<char, int> charFreq(string str)
  {
    return str.Aggregate(
      new Dictionary<char, int>(),
      (dict, c) =>
      {
        int count;
        dict.TryGetValue(c, out count);
        dict[c] = count + 1;
        return dict;
      }
    );
  }
}