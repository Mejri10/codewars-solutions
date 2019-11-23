using System;

public static class AgeDiff 
{
  public static string CalculateAge(int birth, int yearTo) 
  {
    int diff = yearTo - birth;
    if (diff > 0)
      return $"You are {diff} year{(diff > 1 ? "s" :  "")} old.";
    else if (diff < 0)
      return $"You will be born in {-diff} year{(-diff > 1 ? "s" :  "")}.";
    else
      return "You were born this very year!";
  }
}