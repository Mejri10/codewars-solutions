using System;
using System.Linq;

public static class Kata
{
  public static int palindromeChainLength(int n) =>
    palindromeChainLength((long) n);
    
  public static int palindromeChainLength(long n) =>
    IsPalindrome(n) ? 0 : 1 + palindromeChainLength(n + ReverseDigits(n));
  
  private static bool IsPalindrome(long n) =>
    n == ReverseDigits(n);
  
  private static long ReverseDigits(long n) =>
    long.Parse(new string(n.ToString().Reverse().ToArray()));
}