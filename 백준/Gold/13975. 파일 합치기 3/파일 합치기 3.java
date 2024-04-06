import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < T; i++) {
            sb.append(solution(br)).append("\n");
        }
        System.out.print(sb);
    }

    private static long solution(BufferedReader br) throws IOException {
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        PriorityQueue<Long> minHeap = new PriorityQueue<>();
        while (st.hasMoreTokens()){
            minHeap.add(Long.parseLong(st.nextToken()));
        }

        long answer = 0;
        long f1 = minHeap.poll();
        while (!minHeap.isEmpty()) {
            long f2 = minHeap.poll();
            long temp = f1 + f2;
            answer += temp;

            minHeap.add(temp);
            f1 = minHeap.poll();
        }
        return answer;
    }
}