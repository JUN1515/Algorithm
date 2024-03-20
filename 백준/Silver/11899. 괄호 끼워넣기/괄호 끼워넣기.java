import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char [] arr = br.readLine().toCharArray();
        int cnt = 0;
        int left = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == ')') {
                if (left == 0) {
                    cnt++;
                } else {
                    left--;
                }
            } else {
                left++;
            }
        }
        cnt += left;
        System.out.println(cnt);
    }
}
