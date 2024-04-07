import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int t = 0; t < T; t++) {
            sb.append(solution(br)).append("\n");
        }
        System.out.print(sb);
    }

    public static int solution(BufferedReader br) throws IOException {
        int N = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();
        Arrays.sort(arr);

        int maxVal = arr[1] - arr[0];
        for (int i = 3; i < N; i += 2) {
            maxVal = Math.max(maxVal, arr[i] - arr[i - 2]);
        }

        for (int i = 2; i < N; i += 2) {
            maxVal = Math.max(maxVal, arr[i] - arr[i - 2]);
        }
        return maxVal;
    }
}