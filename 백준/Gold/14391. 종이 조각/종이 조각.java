import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int answer = 0;
        int[][] board = new int[n][m];

        for (int i = 0; i < n; i++) {
            char[] c = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                board[i][j] = Character.getNumericValue(c[j]);
            }
        }

        for (int mask = 0; mask < 1 << (n * m); mask++) {
            int rowSum = getRowSum(n, m, mask, board);
            int colSum = getColSum(n, m, mask, board);
            answer = Math.max(answer, rowSum + colSum);
        }

        System.out.println(answer);
    }

    private static int getRowSum(int n, int m, int mask, int[][] board) {
        int result = 0;

        for (int i = 0; i < n; i++) {
            int sum = 0;

            for (int j = 0; j < m; j++) {
                int target = i * m + j;

                if ((mask & (1 << target)) != 0) {
                    sum *= 10;
                    sum += board[i][j];
                } else {
                    result += sum;
                    sum = 0;
                }
            }

            result += sum;
        }

        return result;
    }

    private static int getColSum(int n, int m, int mask, int[][] board) {
        int result = 0;

        for (int j = 0; j < m; j++) {
            int sum = 0;

            for (int i = 0; i < n; i++) {
                int target = i * m + j;

                if ((mask & (1 << target)) == 0) {
                    sum *= 10;
                    sum += board[i][j];
                } else {
                    result += sum;
                    sum = 0;
                }
            }

            result += sum;
        }

        return result;
    }
}