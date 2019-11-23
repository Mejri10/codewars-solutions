public static class Kata
{
  public static bool IsPrime(int n)
  {
    if (n < 2) return false;
    
    bool prime = true;
    for (int i = 2; i * i <= n; i++) 
    {
      if (n % i == 0)
      {
        prime = false;
        break;
      }
    }
    return prime;
  }
}