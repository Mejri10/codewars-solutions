public class Kata
{
  public static bool Check(object[] a, object x)
  {
    foreach (var obj in a)
    { 
      if (obj.Equals(x)) return true;
    }
    return false;
  }
}