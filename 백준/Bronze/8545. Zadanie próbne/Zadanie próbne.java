import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuffer sb = new StringBuffer(sc.nextLine());
        String reverse = sb.reverse().toString();
        
        System.out.println(reverse);
    }
        
}