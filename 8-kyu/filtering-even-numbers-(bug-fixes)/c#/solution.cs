using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
    {
        public static List<int> FilterOddNumber(List<int> listOfNumbers)
        {
            return new List<int>(listOfNumbers.Where(n => n % 2 == 1));
        }
    }