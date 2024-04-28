import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int ds, ys, dm, ym;
        ds = scanner.nextInt();
        ys = scanner.nextInt();
        dm = scanner.nextInt();
        ym = scanner.nextInt();

        int sunYear = ys - ds;
        int moonYear = ym - dm;

        while (sunYear != moonYear) {
            if (sunYear < moonYear) {
                sunYear += ys;
            } else {
                moonYear += ym;
            }
        }
        
        System.out.println(sunYear);
    }
}