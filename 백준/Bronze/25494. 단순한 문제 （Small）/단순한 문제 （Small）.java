import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int minVal = Integer.parseInt(st.nextToken());
            while (st.hasMoreTokens()) {
                minVal = Math.min(minVal, Integer.parseInt(st.nextToken()));
            }
            sb.append(minVal).append("\n");
        }
        System.out.print(sb);
    }
}