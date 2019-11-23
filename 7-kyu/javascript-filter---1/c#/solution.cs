using System;
using System.Linq;

public class Kata
{
  public static string[][] search_names(string[][] logins) =>
    logins.Where(pair => pair[0].EndsWith("_")).ToArray();
}