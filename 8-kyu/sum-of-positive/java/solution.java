public class Positive{

  public static int sum(int[] arr){
    int total = 0;
    for (int i = 0; i < arr.length; i++){
      total += Math.max(arr[i], 0);
    }
    return total;
  }

}