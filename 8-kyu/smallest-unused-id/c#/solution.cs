using System.Linq;
using System.Collections.Generic;

public class Kata
{
  public static int NextId(int[] ids)
  {
    ISet<int> idSet = new HashSet<int>(ids);
    int i = 0;
    while (idSet.Contains(i)) i++;
    return i;
  }
}