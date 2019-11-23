public class Kata
{
  public static string GetPlanetName(int id)
  {
    return new[]
    {
      "Mercury", "Venus", "Earth",
      "Mars", "Jupiter", "Saturn",
      "Uranus", "Neptune"
    }[id - 1];
  }
}