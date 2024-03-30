import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int MaxMulCount = 0;
        int addCount = 0;

        while (st.hasMoreTokens()) {

            int val = Integer.parseInt(st.nextToken());
            int mulCount = 0;

            while (val != 0) {
                if (val % 2 == 1) {
                    addCount++;
                    val--;
                } else {
                    val /= 2;
                    mulCount++;
                }
            }
            if (MaxMulCount < mulCount) MaxMulCount = mulCount;
        }
        System.out.println(addCount + MaxMulCount);
    }
}
