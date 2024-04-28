import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        while (true) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0) break;

            long temp = 0L;
            for (long i = 1L; i <= num; i++) {
                temp += i;
            }
            sb.append(temp).append("\n");
        }
        System.out.print(sb);
    }
}