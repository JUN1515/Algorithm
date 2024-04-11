import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        char[][] charArr = makeArray(N, M);
        int[][] diff = makeArray(N, M, charArr);

        System.out.println(solution(N, M, diff));
    }

    private static char[][] makeArray(int N, int M) throws IOException {
        char[][] arr = new char[N][M];
        for (int r = 0; r < N; r++) {
            String str = br.readLine();
            for (int c = 0; c < M; c++ ) {
                arr[r][c] = str.charAt(c);
            }
        }
        return arr;
    }

    private static int[][] makeArray(int N, int M, char[][] charArr) throws IOException {
        int[][] arr = new int[N][M];
        for (int r = 0; r < N; r++) {
            String str = br.readLine();
            for (int c = 0; c < M; c++) {
                arr[r][c] = (charArr[r][c] == str.charAt(c)) ? 0 : 1;
            }
        }
        return arr;
    }

    private static int solution(int N, int M, int[][] arr) {
        int result = 0;
        if (N >= 3 && M >= 3) {
            for (int r = 0; r < N - 2; r++) {
                for (int c = 0; c < M - 2; c++) {
                    if (arr[r][c] == 1) {
                        changeOperator(r, c, arr);
                        result++;
                    }
                }
            }
        }

        if (!isValidation(N, M, arr)) result = -1;
        return result;
    }

    private static void changeOperator(int r, int c, int[][] arr) {
        for (int i = r; i < r + 3; i++) {
            for (int j = c; j < c + 3; j++) {
                arr[i][j] = (arr[i][j] == 1) ? 0 : 1;
            }
        }
    }

    private static boolean isValidation(int N, int M, int[][] arr) {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (arr[r][c] == 1) return false;
            }
        }
        return true;
    }
}
