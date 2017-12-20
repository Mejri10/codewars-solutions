public class Kata {
  public static int[] pipeFix(int[] numbers) {
    int min = numbers[0];
    int max = numbers[numbers.length - 1];
    int[] arr = new int[max - min + 1];    
    for (int i = 0, j = min; i < arr.length; i++, j++) {
      arr[i] = j;
    }    
    return arr;    
  }
}