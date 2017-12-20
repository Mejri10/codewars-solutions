import java.util.Arrays;

public class Fracts {

    public static String convertFrac(long[][] lst) {
        long[] numerators = getNumerators(lst);
        long[] denominators = getDenominators(lst);
        
        long D = Arrays.stream(denominators)
                       .reduce(1, (x, y) -> lcm(x, y));
        
        long[] Ns = new long[lst.length];
        for (int i = 0; i < lst.length; i++) {
            Ns[i] = numerators[i] * (D / denominators[i]);
        }
        
        StringBuilder sb = new StringBuilder();
        for (long N : Ns) {
            sb.append(String.format("(%d,%d)", N, D));
        }
        
        return sb.toString();
    }

    private static long[] getNthElementFromEachListInAList(long[][] lst, int index) {
        long[] element = new long[lst.length];
        for (int i = 0; i < lst.length; i++) {
            element[i] = lst[i][index];
        }
        return element;
    }
    
    private static long[] getNumerators(long[][] lst) {
        return getNthElementFromEachListInAList(lst, 0);
    }
    
    private static long[] getDenominators(long[][] lst) {
        return getNthElementFromEachListInAList(lst, 1);
    }

    private static long lcm(long x, long y) {
        return (x * y) / gcd(x, y);
    }

    private static long gcd(long x, long y) {
        long r = x % y;
        return r == 0 ? y : gcd(y, r);
    }

}
