import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine());
        long[] arr = new long[3];
        arr[0] = Long.parseLong(st.nextToken());
        arr[1] = Long.parseLong(st.nextToken());
        arr[2] = Long.parseLong(st.nextToken());
        
        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder();
        for(long num : arr) {
            sb.append(num).append(" ");
        }
        System.out.println(sb);

        
    }
}