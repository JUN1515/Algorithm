import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<String> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            arr.add(br.readLine());
        }

        Map<Character, Integer> alphabetMap = new HashMap<>();
        for (String s : arr) {
            int sLength = s.length();
            for (int i = 0; i < sLength; i++) {
                char c = s.charAt(i);
                int val = (int) Math.pow(10 ,sLength - i - 1);
                if (alphabetMap.containsKey(c)) {
                    val += alphabetMap.get(c);
                }
                alphabetMap.put(c, val);
            }
        }
        List<Map.Entry<Character, Integer>> lst = new ArrayList<>(alphabetMap.entrySet());
        lst.sort((a, b) -> b.getValue().compareTo(a.getValue()));

        Map<Character, Integer> alphaToNumber = new HashMap<>();
        int num = 9;
        for (Map.Entry<Character, Integer> entry : lst) {
            alphaToNumber.put(entry.getKey(), num);
            num--;
        }

        long answer = 0;
        for (String s: arr) {
            int sLength = s.length();
            for (int i = 0; i < sLength; i++) {
                char c = s.charAt(i);
                answer += (long) alphaToNumber.get(c) * (int) Math.pow(10, sLength - i - 1);
            }
        }
        System.out.println(answer);

    }
}