using System;
using System.Collections.Generic;
using System.Linq;

public abstract class Coin
{
  public abstract string Name { get; }
  public abstract string NamePlural { get; }
  public abstract decimal Value { get; }
}

public class Quarter : Coin
{
  public override string Name => "Quarter";
  public override string NamePlural => "Quarters";
  public override decimal Value => 0.25m;
}

public class Dime : Coin
{
  public override string Name => "Dime";
  public override string NamePlural => "Dimes";
  public override decimal Value => 0.10m;
}

public class Penny : Coin
{
  public override string Name => "Penny";
  public override string NamePlural => "Pennies";
  public override decimal Value => 0.01m;
}

public static class Kata
{
  private static Coin[] Coins = new Coin[] 
  {
    new Quarter(),
    new Dime(),
    new Penny()
  };
  
  public static string GetChange(decimal price, decimal inputMoney) 
  {
    if (price <= 0m || inputMoney > 1m || price > inputMoney)
    {
      return "Invalid input.";
    }
    
    if (price == inputMoney)
    {
      return "No Change.";
    }
    
    var change = inputMoney - price;
    return string.Join(
      ", ",
      Coins.Aggregate(
        new List<string>(),
        (texts, coin) =>
        {
          var numberOfCoins = (int)(change/coin.Value);
          if (numberOfCoins > 0)
          {
            texts.Add(
              $"{numberOfCoins} {numberOfCoins == 1 ? coin.Name : coin.NamePlural}"
            );
            change %= coin.Value;
          }
          return texts;
        }
      )
    ) + ".";
  }
}