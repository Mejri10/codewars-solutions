using System.Linq;

public class Kata
{
  public static string PrintArray(object[] array)
  {
    return string.Join(",", array.Select(o =>
    {
      if (o.GetType().IsArray)
       return PrintArray(o as object[]);

      return o.ToString();
    }));
  }
}