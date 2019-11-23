using System.Linq;

public class Kata
{
  public static string[] AddLength(string str)
  {
    return str.Split(" ")
      .Select(s => $"{s} {s.Length.ToString()}")
      .ToArray();
  }
}