using System.Collections.Generic;

public class Kata
{
  public static string Collatz(int n)
  {
    var numbers = new List<int>();
    while (n > 1)
    {
      numbers.Add(n);
      n = NextCollatzNumber(n);
    }
    numbers.Add(1);
    return string.Join("->", numbers);
  }
  
  private static int NextCollatzNumber(int n)
  {
    return n % 2 == 0 ? n/2 : 3*n + 1;
  }
}