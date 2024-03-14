public class  Main {
    public static void main(String[] args) {

        boolean[] check = new boolean[10001];

        for (int i = 1; i < 10001; i++) {
            int n = d(i);

            if (n < 10001) check[n] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < 10001 ; i++) {
            if (!check[i]) sb.append(i).append('\n');
        }

        System.out.println(sb);
    }

    public static int d(int inputNum) {
        int accSum = inputNum;

        while (inputNum > 0) {
            accSum += inputNum % 10;
            inputNum /= 10;
        }
        return accSum;
    }
}