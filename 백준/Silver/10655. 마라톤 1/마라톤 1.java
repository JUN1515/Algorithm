import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] arr = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        int[] diff_1 = new int[N - 1];
        for (int i = 0; i < N - 1; i++) {
            diff_1[i] = getDistance(arr[i + 1], arr[i]);
        }

        int max_reduction_path = 0;
        for (int i = 0; i < N - 2; i++) {
            int jump_path = getDistance(arr[i + 2], arr[i]);
            int default_path = diff_1[i] + diff_1[i + 1];
            int reduction_path = default_path - jump_path;
            if (max_reduction_path < reduction_path) {
                max_reduction_path = reduction_path;
            }
        }

        int answer = 0;
        for (int value : diff_1) {
            answer += value;
        }
        answer -= max_reduction_path;
        System.out.println(answer);
    }

    private static int getDistance(int[] coord1, int[] coord2) {
        return Math.abs(coord2[0] - coord1[0]) + Math.abs(coord2[1] - coord1[1]);
    }
}