using System.Text.RegularExpressions;

public class Kata
{
  public static string[] Bald(string x) =>
    new[] {removeHairs(x), hairMessage(countHairs(x))};
  
  private static int countHairs(string s) =>
    Regex.Matches(s, "/").Count;
  
  private static string removeHairs(string s) =>
    Regex.Replace(s, "/", "-");
  
  private static string hairMessage(int hairsCount)
  {
    switch (hairsCount)
    {
      case 0:
       return "Clean!";
      case 1:
        return "Unicorn!";
      case 2:
        return "Homer!";
      case 3:
      case 4:
      case 5:
        return "Careless!";
      default:
        return "Hobo!";
    }
  }
}