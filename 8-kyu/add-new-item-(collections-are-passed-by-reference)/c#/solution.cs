using System;
using System.Collections.Generic;

public class AddMore
    {
        public static List<int> AddExtra(List<int> listOfNumbers)
        {
            var newList = new List<int>(listOfNumbers);
            newList.Add(42);
            return newList;
        }
    }