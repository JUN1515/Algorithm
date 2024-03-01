import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());

        for (int i = 1; i <= N * 2 - 1; i++) {
            for (int j = 1; j <= i - ((i % N) * 2) * (i / (N + 1)); j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}