using System.Collections.Generic;

public class Kata
{
  public static List<int> ReverseList(List<int> list)
  {
    var newList = new List<int>(list.Count);
    for (int i = list.Count-1; i >= 0; i--)
    {
      newList.Add(list[i]);
    }
    return newList;
  }
}