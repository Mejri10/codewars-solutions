using System.Collections.Generic;
using System.Linq;

public static class Filter
{
  private static ISet<string> geese =
    new HashSet<string>(
      new[] { "African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher" }
  );

  public static IEnumerable<string> GooseFilter(IEnumerable<string> birds)
  {
    return birds.Except(geese);
  }
}