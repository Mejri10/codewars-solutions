using System.Linq;
using System;

public class Kata
{
  public static bool LogicalCalc(bool[] array, string op)
  {
    return array.Aggregate(operatorFactory(op));
  }
  
  private static Func<bool, bool, bool> operatorFactory(string op)
  {
    Func<bool, bool, bool> opFunc;
    switch(op)
    {
      case "XOR":
        opFunc = (bool a, bool b) => a ^ b;
        break;
      case "AND":
        opFunc = (bool a, bool b) => a && b;
        break;
      case "OR":
        opFunc = (bool a, bool b) => a || b;
        break;
      default:
        goto case "OR";
    }
    return opFunc;
  }
}