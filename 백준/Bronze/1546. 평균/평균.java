import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int maxVal = 0;
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            if (maxVal < arr[i]) maxVal = arr[i];
        }
        double result = 0;
        for (int i = 0; i < N; i++) {
            result += ((double) (arr[i] * 100) / maxVal);
        }
        System.out.println(result / N);

    }
}
