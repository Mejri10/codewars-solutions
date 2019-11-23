// Create the CombineNames method here
public class Kata
{
  public static string CombineNames(params string[] names)
  {
    return string.Join(" ", names);
  }
}