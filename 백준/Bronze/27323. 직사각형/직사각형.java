import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int A = Integer.parseInt(sc.nextLine());
        int B = Integer.parseInt(sc.nextLine());
        System.out.println(A * B);
    }
}