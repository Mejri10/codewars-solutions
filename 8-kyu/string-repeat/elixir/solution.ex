using System.Text;

namespace Solution
{
  public static class Program
  {
    public static string repeatStr(int n, string s)
    {
      var strBuilder = new StringBuilder();
      for (int i = 0; i < n; i++)
        strBuilder.Append(s);
      return strBuilder.ToString();
    }
  }
}