import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int num1, num2;
        num1 = Integer.parseInt(st.nextToken());
        num2 = Integer.parseInt(st.nextToken());;

        int small;
        int big;

        if (num1 > num2) {
            big = num1;
            small = num2;
        } else {
            big = num2;
            small = num1;
        }

        int gcd = 1;    //최대공약수

        for (int i = 1; i <= small; i++) {
            if (big % i == 0 && small % i == 0) gcd = i;
        }

        int lcm = num1 * num2 / gcd;    //최소공배수

        System.out.println(gcd);
        System.out.println(lcm);
    }
}