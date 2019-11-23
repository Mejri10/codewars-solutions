using System.Numerics;
using System.Linq;

public class Kata
{
  public static BigInteger[] PowersOfTwo(int n)
  {
    return Enumerable.Range(0, n+1)
     .Select(e => new BigInteger(1) << e)
     .ToArray();
  }
}