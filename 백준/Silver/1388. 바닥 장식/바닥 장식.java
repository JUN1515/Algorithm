import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int count = 0;

        String[][] arr = new String[N][M];
        for (int i = 0; i < N; i++) {
            arr[i] = br.readLine().split("");
        }

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (arr[r][c].equals("-")) {
                    dfs_row(r, c, M, arr);
                    count++;
                } else if (arr[r][c].equals("|")) {
                    dfs_col(r, c, N, arr);
                    count++;
                }
            }
        }
        System.out.println(count);

    }

    public static void dfs_row(int r, int  c, int M, String[][]arr) {
        arr[r][c] = ".";
        List<int[]> S = new ArrayList<>();
        S.add(new int[]{r, c});

        while (!S.isEmpty()) {
            int[] s = S.remove(S.size() - 1);
            r = s[0];
            c = s[1];

            for (int dc : new int[]{-1, 1}) {
                int nc = c + dc;
                if ((nc < 0) || (nc >= M)) continue;
                if (arr[r][nc].equals("-")) {
                    arr[r][nc] = ".";
                    S.add(new int[]{r, nc});
                }
            }
        }
    }

    public static void dfs_col(int r, int  c, int N, String[][]arr) {
        arr[r][c] = ".";
        List<int[]> S = new ArrayList<>();
        S.add(new int[]{r, c});

        while (!S.isEmpty()) {
            int[] s = S.remove(S.size() - 1);
            r = s[0];
            c = s[1];

            for (int dr : new int[]{-1, 1}) {
                int nr = r + dr;
                if ((nr < 0) || (nr >= N)) continue;
                if (arr[nr][c].equals("|")) {
                    arr[nr][c] = ".";
                    S.add(new int[]{nr, c});
                }
            }
        }
    }
}
