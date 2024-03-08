import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        // 입력값 범위 : -4000 ~ 4000
        int[] arr = new int[8001];

        int sum = 0;    // 총합계
        int max = Integer.MIN_VALUE;    //최댓값
        int min = Integer.MAX_VALUE;    //최솟값
        int median = 4001;              //중앙값
        int mode = 4001;                //최빈값

        for (int i = 0; i < N; i++) {
            int value = Integer.parseInt(br.readLine());
            sum += value;
            arr[value + 4000]++;

            if (max < value) max = value;
            if (min > value) min = value;
        }

        //순회
        int count = 0;      //중앙값 빈도 누적수
        int mode_max = 0;   //최빈값의 최대값

        //이전의 동일한 최빈값이 1번만 등장했을 경우 true, 아닐경우 false
        boolean flag = false;

        for (int i = min + 4000; i <= max + 4000; i++) {
            if (arr[i] == 0) continue;

            //중앙값 찾기 - 누적횟수가 전체 길이 절반에 못 미치는 경우
            if (count < (N + 1) / 2) {
                count += arr[i];
                median = i - 4000;
            }

            //최빈값 찾기 - 이전 최빈값보다 현재 값의 빈도수가 더 높을 경우
            if (mode_max < arr[i]) {
                mode_max = arr[i];
                mode = i - 4000;
                flag = true;        // 첫 등장이기에 true로 변경
            } else if (mode_max == arr[i] && flag == true) {
                mode = i - 4000;
                flag = false;
            }
        }

        System.out.println((int)Math.round((double) sum / N));
        System.out.println(median); // 중앙값
        System.out.println(mode);   // 최빈값
        System.out.println(max - min);  //범위
    }
}
