import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();

        String answer = "Error";
        if (A + B + C == 180) {
            if (A == B && B == C) {
                answer = "Equilateral";
            } else {
                answer = (A == B || A == C || B == C) ? "Isosceles" : "Scalene";
            }
        }
        System.out.println(answer);
    }
}