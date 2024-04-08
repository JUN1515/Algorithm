import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int t = 0; t < T; t++) {
            sb.append(solution(br)).append("\n");
        }
        System.out.print(sb);
    }

    public static String solution(BufferedReader br) throws IOException{
        int N = Integer.parseInt(br.readLine());
        List<Integer> arr = new ArrayList<>();
        arr.add(0);
        arr.add(1);

        int n = 1;

        while (arr.get(n) < N) {
            arr.add(arr.get(n) + arr.get(n-1));
            n++;
        }

        List<Integer> answer = new ArrayList<>();

        for (int i = n; i >= 0; i--) {
            if (N < arr.get(i)) continue;
            answer.add(arr.get(i));

            if (N == arr.get(i)) break;
            N -= arr.get(i);
        }

        String output =  answer.stream()
                            .sorted(Comparator.naturalOrder())
                            .map(Object::toString)
                            .collect(Collectors.joining(" "));

        return output;
    }
}