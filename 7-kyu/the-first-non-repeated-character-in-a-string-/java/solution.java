import java.util.*;

public class FirstNonRepeated {

    public static char firstNonRepeated(String source) {    
      Map<Character, Integer> dict = new HashMap<Character, Integer>();
      for (char c : source.toCharArray()) {
        dict.put(c, dict.getOrDefault(c, 0) + 1);
      }      
      char returnChar = source.charAt(0);
      for (int i = 0; i < source.length(); i++) {
        if (dict.get(source.charAt(i)) == 1) {
          returnChar = source.charAt(i);
          break;
        }
      }
      return returnChar;
    }
}