import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = readInt();
        int[] array = new int[N];

        for (int i = 0; i < N; i++) {
            array[i] = readInt();
        }

        int max = array[0], min = array[0];

        for (int i = 1; i < N; i++) {
            max = Math.max(max, array[i]);
            min = Math.min(min, array[i]);
        }

        StringBuilder sb = new StringBuilder();
        sb.append(min).append(" ").append(max);
        System.out.println(sb);
    }

    private static int readInt() throws IOException {
        int val = 0;
        int total = 0;
        int sign = 1;

        while ((val = System.in.read()) != '\n' && val != ' ') {
            if (val == '-') sign = -1;
            else total = total * 10 + (val - '0');
        }

        if (sign == -1) total = -total;

        return total;
    }
}