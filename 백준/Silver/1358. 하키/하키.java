import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int w;
    private static int h;
    private static int x;
    private static int y;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        int answer = 0;

        for (int i = 0; i < p; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            answer += check(x1, y1);
        }
        System.out.println(answer);
    }

    private static int check(int x1, int y1) {
        if (y1 < y || y1 > y + h) return 0;
        if (x1 >= x && x1 <= x + w) return 1;
        else if (x1 < x && Math.pow(x1 - x, 2) + Math.pow(y1 - (y + (h / 2)), 2) <= Math.pow(h / 2, 2)) return 1;
        else if (x1 > x + w && Math.pow(x1 - (x + w), 2) + Math.pow(y1 - (y + (h / 2)), 2) <= Math.pow(h / 2, 2)) return 1;
        else return 0;
    }
}