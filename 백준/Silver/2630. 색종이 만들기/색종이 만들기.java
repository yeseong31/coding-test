import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    private static void compress(int n, int x, int y, int[][] board, int[] answer) {
        int k = n / 2;
        int v = board[x][y];

        for (int i = x; i < x + n; i++) {
            for (int j = y; j < y + n; j++) {
                if (board[i][j] != v) {
                    compress(k, x, y, board, answer);
                    compress(k, x + k, y, board, answer);
                    compress(k, x, y + k, board, answer);
                    compress(k, x + k, y + k, board, answer);
                    return;
                }
            }
        }

        ++answer[v];
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[] answer = {0, 0};
        compress(n, 0, 0, board, answer);

        sb.append(answer[0]).append('\n').append(answer[1]);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}