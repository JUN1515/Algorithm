import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String number = "";
        while (!(number = br.readLine()).equals("0")) {
            int N = number.length();
            boolean check = true;
            int left = 0;
            int right = N - 1;

            while (left < right) {
                if (number.charAt(left++) != number.charAt(right--)) {
                    check = false;
                    break;
                }
            }

            sb.append((check) ? "yes" : "no").append("\n");
        }
        System.out.println(sb);
    }
}