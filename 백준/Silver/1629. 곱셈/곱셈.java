import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static long c;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        c = Long.parseLong(st.nextToken());

        System.out.println(pow(a, b));
    }

    public static long pow(long a, long exponent) {
        // 지수가 1일 경우 a^1 = a 이므로, a를 리턴
        if (exponent == 1) return a % c;
        long temp = pow(a, exponent/2);
        return (exponent % 2 == 1) ? (temp * temp % c) * a % c : (temp * temp) % c;
    }
}
