public class Kata
{
  public static double? ParseF(object s = null)
  {
    double valueParsed;
    if (double.TryParse((s as string), out valueParsed))
      return valueParsed;

    return null;
      
  }
}