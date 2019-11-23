using System.Collections.Generic;

public static class Kata
{
  public static string StringifyDict<TKey, TValue>(Dictionary<TKey, TValue> hash)
  {
    List<string> entries = new List<string>(hash.Keys.Count);
    foreach(var entry in hash)
      entries.Add($"{entry.Key} = {entry.Value}");

    return string.Join(",", entries);
  }
}