using System.Linq;

public class Kata
{
  public static int SumMix(object[] x)
  {
    return x.Sum(e => e is string ? int.Parse((string) e) : (int) e);
  }
}