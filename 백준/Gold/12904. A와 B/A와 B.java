import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String t = br.readLine();

        String sReverse = new StringBuilder(s).reverse().append("B").toString();

        int sLength = s.length();
        int tLength = t.length();

        int[] countArr = new int[tLength];
        if (t.charAt(0) == 'B') countArr[0] = 1;
        for (int i = 1; i < tLength; i++) {
            if (t.charAt(i) == 'B') countArr[i]++;
            countArr[i] += countArr[i - 1];
        }

        int answer = 0;
        for (int i = 0; i <= tLength - sLength; i++) {
            if (t.substring(i, i + sLength).equals(s)) {
                if (!check_B(i - 1, i + sLength, tLength, countArr)) continue;
                if (check_A(i - 1, t)) {
                    answer = 1;
                    break;
                }
            }
        }

        if (answer == 0) {
            for (int i = 0; i < tLength - sLength; i++) {
                if (t.substring(i, i + sLength + 1).equals(sReverse)) {
                    if (!check_B(i - 1, i + sLength + 1, tLength, countArr)) continue;
                    answer = 1;
                    break;
                }
            }
        }

        System.out.println(answer);
    }

    public static boolean check_A(int leftEnd, String t) {
        if (leftEnd >= 0) {
            for (int i = leftEnd; i >= 0; i--) {
                if (t.charAt(i) == 'A') {
                    if (i != leftEnd && t.charAt(i + 1) == 'B') break;
                    return false;
                }
            }
        }
        return true;
    }

    public static boolean check_B(int leftEnd, int rightStart, int tLength, int[] countArr) {
        if (leftEnd < 0) {
            return  countArr[tLength - 1] - countArr[rightStart - 1] == 0;
        }
        return countArr[leftEnd] == countArr[tLength - 1] - countArr[rightStart - 1];
    }

}