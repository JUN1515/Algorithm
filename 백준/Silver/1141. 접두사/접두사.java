import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Comparator;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<String> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            arr.add(br.readLine());
        }
        arr.sort(Comparator.reverseOrder());

        int answer = N;
        for (int i = 1; i < N; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (arr.get(i).charAt(0) != arr.get(j).charAt(0)) break;
                if (arr.get(i).length() > arr.get(j).length()) break;
                if (arr.get(i).equals(arr.get(j).substring(0, arr.get(i).length()))) {
                    answer--;
                    break;
                }
            }
        }

        System.out.println(answer);
    }
}
