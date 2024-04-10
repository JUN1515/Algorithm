import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int t = 1;;t++) {
            String word = br.readLine();
            if (word.charAt(0) == '-') break;

            int count = 0;
            int stack = 0;

            for (char ch: word.toCharArray()) {
                switch (ch) {
                    case '{':
                        stack++;
                        break;
                    case '}':
                    {
                        if (stack == 0) {
                            count++;
                            stack++;
                        } else {
                            stack--;
                        }
                    }
                }
            }

            count += stack / 2;
            sb.append(t).append(". ").append(count).append("\n");
        }

        System.out.print(sb);
    }
}
