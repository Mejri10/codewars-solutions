using System;
using System.Linq;

public static class Kata
{
    public static int GetVowelCount(string str)
    {
        int vowelCount = 0;
        const string vowels = "aeiou";

        foreach(var c in str)
        {
          if(vowels.Contains(c)) vowelCount++;
        }

        return vowelCount;
    }
}
