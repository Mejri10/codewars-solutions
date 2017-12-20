import java.util.*;

public class AreSame {

    public static boolean comp(int[] a, int[] b) {
        if (a == null || b == null)  return false;
        
        Set<Integer> setASquared = new HashSet<>();
        Set<Integer> setB = new HashSet<>();
        
        int[] aSquared = Arrays.stream(a).map(x -> x * x).toArray();
        
        addToSet(setASquared, aSquared);
        addToSet(setB, b);

        return setASquared.equals(setB);
    }
    
    private static void addToSet(Set<Integer> set, int[] array) {
      for (int n : array) {
        set.add(n);
      }
    }
}