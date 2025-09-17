import java.io.*;

public class Main {
    private static final int MAX_SIZE = 2001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[MAX_SIZE][MAX_SIZE];

        for (int i = 1; i <= n; i++) {
            String line = br.readLine();
            for (int j = 1; j <= n; j++) {
                board[i][j] = line.charAt(j - 1) - '0';
            }
        }

        int count = solution(n, board);

        sb.append(count);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int solution(int n, int[][] board) {
        int count = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (board[i][j] != 1) continue;

                int maxK = Math.min(Math.min(i - 1, n - i), Math.min(j - 1, n - j));

                for (int k = 1; k <= maxK; k++) {
                    if (isValidPlus(board, i, j, k)) {
                        count++;
                    } else {
                        break;
                    }
                }
            }
        }

        return count;
    }

    private static boolean isValidPlus(int[][] board, int centerI, int centerJ, int k) {
        for (int i = centerI - k; i <= centerI + k; i++) {
            for (int j = centerJ - k; j <= centerJ + k; j++) {
                if (i == centerI || j == centerJ) {
                    if (board[i][j] != 1) return false;
                } else {
                    if (board[i][j] != 0) return false;
                }
            }
        }

        return true;
    }
}