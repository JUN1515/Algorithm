import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String S = st.nextToken();
        String E = st.nextToken();
        String Q = st.nextToken();
        String log = "";

        String time = "";
        String name = "";

        Set<String> check = new HashSet<>();
        int answer = 0;

        while ((log = br.readLine()) != null) {
            String[] strarr = log.split(" ");
            time = strarr[0];
            name = strarr[1];

            if (timeCompare(S, time)) {
                check.add(name);
            } else if (timeCompare(time, E) && timeCompare(Q, time)) {
                if (check.contains(name)) {
                    answer++;
                    check.remove(name);
                }
            }
        }
        System.out.println(answer);
        
    }

    public static boolean timeCompare(String time1, String time2) {
        int m1 = Integer.parseInt(time1.substring(0, 2)) * 60 + Integer.parseInt(time1.substring(3));
        int m2 = Integer.parseInt(time2.substring(0, 2)) * 60 + Integer.parseInt(time2.substring(3));
        return m1 >= m2;
    }
}