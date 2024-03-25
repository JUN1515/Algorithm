import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String answer = "";
        switch (s) {
            case "M":
                answer = "MatKor";
                break;
            case "W":
                answer = "WiCys";
                break;
            case "C":
                answer = "CyKor";
                break;
            case "A":
                answer = "AlKor";
                break;
            case "$":
                answer = "$clear";
                break;
        }
        System.out.println(answer);
    }
}