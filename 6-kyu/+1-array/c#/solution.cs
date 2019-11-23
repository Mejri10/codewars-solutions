using System;
using System.Linq;
using System.Collections.Generic;

namespace Kata
{
  public static class Kata
  {
    public static int[] UpArray(int[] num)
		{
      if (!ArrayIsValid(num))
        return null;

      return UpArrayHelper(new List<int>(num), num.Length - 1).ToArray();
    }
    
    public static List<int> UpArrayHelper(List<int> arr, int index)
    {
      if (arr[index] == 9)
      {
        arr[index] = 0;
        if (index == 0)
        {
          arr.Insert(0, 1);
        } else 
        {
          UpArrayHelper(arr, index - 1);
        }
      } else
      {
        arr[index]++;
      }
      
      return arr;
    }
    
    public static bool ArrayIsValid(int[] arr)
    {
      return arr.Length > 0 && arr.All(n => n >= 0 && n < 10);
    }
  }
}