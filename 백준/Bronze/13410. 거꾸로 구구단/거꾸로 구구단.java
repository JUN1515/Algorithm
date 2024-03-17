import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] arr = new int[K + 1];

        for (int i = 1; i <= K; i++) {
            int val = N * i;

            int reVal = 0;
            while (val > 0) {
                reVal = reVal * 10 + val % 10;
                val /= 10;
            }
            arr[i] = reVal;
        }

        int answer = 0;
        for (int i = 1; i <= K; i++) {
            answer = Math.max(answer, arr[i]);
        }

        System.out.println(answer);
    }
}