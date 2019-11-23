using System.Collections.Generic;

public class Kata
{
  public static Dictionary<char, int> CharFreq(string message)
  {
    var charFreq = new Dictionary<char, int>();
    foreach(var c in message)
    {
      int count = 0;
      charFreq.TryGetValue(c, out count);
      charFreq[c] = count + 1;
    }
    return charFreq;
  }
}