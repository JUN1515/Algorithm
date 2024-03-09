import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int inputNum = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        br.close();

        ArrayList<Character> list = new ArrayList<>();

        while (inputNum > 0) {
            if (inputNum % B < 10) list.add((char) (inputNum % B + '0'));
            else list.add((char) (inputNum % B - 10 + 'A'));
            inputNum /= B;
        }

        for (int i = list.size() - 1; i >= 0; i--) System.out.print(list.get(i));
    }
}