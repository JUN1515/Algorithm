import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n1 = Integer.parseInt(br.readLine());
        int n2 = Integer.parseInt(br.readLine());
        int n3 = Integer.parseInt(br.readLine());

        int n = n1 * n2 * n3;
        int arr[] = new int[10];

        StringBuilder sb = new StringBuilder();

        while (n > 0) {
            arr[n % 10]++;
            n /= 10;
        }

        for (int num : arr) {
            sb.append(num).append("\n");
        }
        System.out.println(sb);
    }
}
