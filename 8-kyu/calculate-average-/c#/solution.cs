using System;

class AverageSolution
{
  public static double FindAverage(double[] array)
  {
    var sum = 0.0;
    foreach(var n in array)
      sum += n;
    return sum/(Math.Max(1, array.Length));
  }
} 