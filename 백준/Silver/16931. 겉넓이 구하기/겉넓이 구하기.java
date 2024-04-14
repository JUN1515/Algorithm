import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int up = N * M;

        int left = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (j == 0) {
                    left += arr[i][j];
                } else {
                    if (arr[i][j - 1] < arr[i][j]) {
                        left += arr[i][j] - arr[i][j - 1];
                    }
                }
            }
        }

        int front = 0;
        for (int j = 0; j < M; j++) {
            for (int i = 0; i < N; i++) {
                if (i == 0) {
                    front += arr[i][j];
                } else {
                    if (arr[i - 1][j] < arr[i][j]) {
                        front += arr[i][j] - arr[i - 1][j];
                    }
                }
            }
        }

        int answer = 2 * (up + left + front);
        bw.write(Integer.toString(answer));
        bw.newLine();

        br.close();
        bw.close();
    }
}