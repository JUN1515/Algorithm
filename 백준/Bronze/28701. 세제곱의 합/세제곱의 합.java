import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = Long.parseLong(sc.nextLine());

        long sumN = 0;
        long sumTN = 0;
        for (int i = 1; i <= N; i++) {
            sumN += i;
            sumTN += (i * i * i);
        }

        StringBuilder sb = new StringBuilder();
        sb.append(sumN).append("\n");
        sb.append(sumN * sumN).append("\n");
        sb.append(sumTN);
        System.out.println(sb);
    }
}
