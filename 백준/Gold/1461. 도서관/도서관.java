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
        int M = Integer.parseInt(st.nextToken());

        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int book = Integer.parseInt(st.nextToken());
            if (book < 0) {
                left.add(-book);
            } else {
                right.add(book);
            }
        }

        int answer = 0;
        int idx;
        left.sort(Comparator.reverseOrder());
        right.sort(Comparator.reverseOrder());
        for (int i = 0; i < left.size() / M; i++) {
            answer += (left.get(i * M) * 2);
        }

        if ((idx = left.size() % M) != 0) {
            answer += (left.get(left.size() - idx) * 2);
        }

        for (int i = 0; i < right.size() / M; i++) {
            answer += (right.get(i * M) * 2);
        }
        if ((idx = right.size() % M) != 0) {
            answer += (right.get(right.size() - idx) * 2);
        }

        if (left.isEmpty()) {
            answer -= right.get(0);
        } else if (right.isEmpty()) {
            answer -= left.get(0);
        } else {
            answer -= (left.get(0) > right.get(0)) ? left.get(0) : right.get(0);
        }
        System.out.println(answer);

    }
}