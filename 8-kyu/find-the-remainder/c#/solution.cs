using System;

public class Kata
{
  public static int Remainder(int a, int b)
  {
    int min = Math.Min(a, b);
    int max = Math.Max(a, b);
    
    if (min == 0)
      throw new DivideByZeroException();
    
    return max % min;
  }
}