import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    private static char[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        board = new char[n][2 * n - 1];
        for (char[] row : board) {
            Arrays.fill(row, ' ');
        }

        dfs(0, n - 1, n);

        for (char[] row : board) {
            System.out.println(String.valueOf(row));
        }
    }

    private static void dfs(int x, int y, int k) {
        if (k <= 3) {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < i + 1; j++) {
                    board[x + i][y + j] = '*';
                    board[x + i][y - j] = '*';
                }
                board[x + 1][y] = ' ';
            }
            return;
        }

        k /= 2;
        dfs(x, y, k);
        dfs(x + k, y - k, k);
        dfs(x + k, y + k, k);
    }
}