import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        int max = -1000000;
        int min = 1000000;
        for (int i = 0; i < N; i++) {
            int number = Integer.parseInt(st.nextToken());
            if (max < number) max = number;
            if (min > number) min = number;
        }
        System.out.println(min + " " + max);
    }
}