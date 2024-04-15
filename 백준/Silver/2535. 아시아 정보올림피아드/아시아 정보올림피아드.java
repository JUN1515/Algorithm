import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        List<int[]> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String[] line = scanner.nextLine().split(" ");
            int a = Integer.parseInt(line[0]);
            int b = Integer.parseInt(line[1]);
            int s = Integer.parseInt(line[2]);
            arr.add(new int[]{a, b, s});
        }

        Collections.sort(arr, (x, y) -> Integer.compare(y[2], x[2]));

        List<int[]> answer = new ArrayList<>();
        Map<Integer, Integer> dic = new HashMap<>();
        int count = 0;
        for (int[] values : arr) {
            int a = values[0];
            int b = values[1];
            if (dic.getOrDefault(a, 0) == 2) continue;
            answer.add(new int[]{a, b});
            dic.put(a, dic.getOrDefault(a, 0) + 1);
            count++;
            if (count == 3) {
                break;
            }
        }

        for (int i = 0; i < 3; i++) {
            int[] pair = answer.get(i);
            System.out.println(pair[0] + " " + pair[1]);
        }
    }
}