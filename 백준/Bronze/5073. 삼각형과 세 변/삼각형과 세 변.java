import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static StringTokenizer st;
    private static int total;
    private static int A;
    private static int B;
    private static int C;
    private static int maxVal;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        total = 0;
        do {
            st = new StringTokenizer(br.readLine());
            A = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());

            total = A + B + C;
            if (total == 0) break;

            maxVal = Math.max(Math.max(A, B), C);
            if (maxVal < total - maxVal) {
                if (A == B && A == C) {
                    sb.append("Equilateral");
                } else if (A == B || A == C || B == C) {
                    sb.append("Isosceles");
                } else {
                    sb.append("Scalene");
                }
            } else {
                sb.append("Invalid");
            }
            sb.append("\n");
        } while (true);
        System.out.print(sb);
    }
}
