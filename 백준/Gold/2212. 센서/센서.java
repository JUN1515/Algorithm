import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int K = Integer.parseInt(br.readLine());
		
		int[] arr = Arrays.stream(br.readLine().split(" "))
							.mapToInt(Integer::parseInt)
							.toArray();
		Arrays.sort(arr);
		
		List<Integer> diff = new ArrayList<Integer>();
		for (int i = 1; i < N; i++) {
			diff.add(arr[i] - arr[i - 1]);
		}
		diff.sort(Comparator.reverseOrder());
		
		int sum = 0;
		if (K <= N) {
			sum = diff.subList(K-1, N-1).stream().mapToInt(Integer::intValue).sum();
		}
        
		System.out.println(sum);
		
	}

}