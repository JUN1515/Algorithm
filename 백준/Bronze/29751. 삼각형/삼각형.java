import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine());
        
        double W = Integer.parseInt(st.nextToken());        
        double H = Integer.parseInt(st.nextToken());
        
        double answer = (W * H)/2;
        System.out.println(String.format("%.1f", answer));
    }
}