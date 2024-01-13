import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int maxVal = 0;
        int number = 0;

        for (int i = 1; i <= 9; i++) {
            int inputVal = Integer.parseInt(br.readLine());
            if (maxVal < inputVal) {
                maxVal = inputVal;
                number = i;
            }
        }
        sb.append(maxVal).append("\n").append(number).append("\n");
        System.out.println(sb);
    }
}