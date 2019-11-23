using System;
using System.Linq;

public class Kata {
  public static char AddLetters(char[] letters) {
    var total = letters.Sum(c => (int)c - 96);
    return total % 26 == 0 ? 'z' : (char)(96 + (total % 26));
  }
}