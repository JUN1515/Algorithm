import java.math.BigInteger;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine());
        BigInteger A = new BigInteger(st.nextToken());
        BigInteger B = new BigInteger(st.nextToken());
        System.out.println(A.multiply(B));
    }
}
