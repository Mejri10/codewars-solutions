using System.Linq;

public class Kata
{
  public static string Shortcut(string input)
  {
    var vowels = new[] {'a', 'e', 'i', 'o', 'u'};
    return string.Join("", input.Where(c => !vowels.Contains(c)));
  }
}