public class Bob {
  public static int enough(int cap, int on, int wait){
    return Math.max(wait - (cap - on), 0);
  }
}