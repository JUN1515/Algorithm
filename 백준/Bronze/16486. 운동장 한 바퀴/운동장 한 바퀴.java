import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double PI = 3.141592;
        double d1 = sc.nextDouble();
        sc.nextLine();
        double d2 = sc.nextDouble();
        sc.nextLine();
        double answer = (d1 * 2) + (2 * PI * d2);
        System.out.println(answer);
    }
}