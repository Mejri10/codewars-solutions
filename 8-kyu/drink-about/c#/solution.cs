public interface Person
{
  string drink();
}

public class Kid : Person
{
  public string drink()
  {
    return "drink toddy";
  }
}

public class Teen : Person
{
  public string drink()
  {
    return "drink coke";
  }
}

public class YoungAdult : Person
{
  public string drink()
  {
    return "drink beer";
  }
}

public class Adult : Person
{
  public string drink()
  {
    return "drink whisky";
  }
}

public static class PersonFactory
{
  public static Person FromDrinkingAge(int age)
  {
    if (age < 14)
      return new Kid();
    else if (age < 18)
      return new Teen();
    else if (age < 21)
      return new YoungAdult();
    else
      return new Adult();
  }
}

public class Kata
{
  public static string PeopleWithAgeDrink(int old)
  {
    return PersonFactory.FromDrinkingAge(old).drink();
  }
}