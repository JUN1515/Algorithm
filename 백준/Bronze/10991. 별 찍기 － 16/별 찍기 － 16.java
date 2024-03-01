import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        int mod = N % 2;

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N + i - 1 ; j++) {
                if (j <= N - i) {
                    System.out.print(" ");
                } else {
                    if (j % 2 == mod) System.out.print("*");
                    else System.out.print(" ");
                }
            }
            mod = (mod + 1) % 2;
            System.out.println();
        }
    }
}