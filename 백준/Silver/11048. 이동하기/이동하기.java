import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (i == 0 && j >= 1) {
                    board[i][j] += board[i][j - 1];
                }
                if (j == 0 && i >= 1) {
                    board[i][j] += board[i - 1][j];
                }
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                board[i][j] += Math.max(Math.max(board[i - 1][j], board[i - 1][j - 1]), board[i][j - 1]);
            }
        }

        sb.append(board[n - 1][m - 1]);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}