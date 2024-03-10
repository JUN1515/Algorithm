import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        char[] arr;
        arr = input.toCharArray();

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] >= 'a' && arr[i] <= 'z') {
                arr[i] = (char) (arr[i] + 'A' - 'a');
            }
            else if (arr[i] >= 'A' && arr[i] <= 'Z') {
                arr[i] = (char) (arr[i] - ('A' - 'a'));
            }
        }

        System.out.println(arr);
    }
}