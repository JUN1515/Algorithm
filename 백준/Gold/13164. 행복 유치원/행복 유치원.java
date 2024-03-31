import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        String[] arr = br.readLine().split(" ");

        List<Integer> diff = new ArrayList<>();
        for (int i = 1; i < N; i++) {
            diff.add(Integer.parseInt(arr[i]) - Integer.parseInt(arr[i - 1]));
        }
        diff.sort(Comparator.reverseOrder());
        int sum = diff.subList(K-1, N-1).stream().mapToInt(Integer::intValue).sum();
        System.out.println(sum);
    }
}
