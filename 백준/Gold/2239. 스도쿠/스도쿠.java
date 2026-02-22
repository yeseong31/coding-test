import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    static final int N = 9;
    static final int FULL = (1 << 10) - 2;

    static int[][] board = new int[N][N];

    static int[] rowMask = new int[N];
    static int[] colMask = new int[N];
    static int[] boxMask = new int[N];

    static int[] emptiesR = new int[N * N];
    static int[] emptiesC = new int[N * N];
    static int emptyCount = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            line = line.replaceAll("\\s+", "");
            while (line.isEmpty()) {
                line = br.readLine();
                line = line.replaceAll("\\s+", "");
            }

            for (int j = 0; j < N; j++) {
                int v = line.charAt(j) - '0';
                board[i][j] = v;
                if (v == 0) {
                    emptiesR[emptyCount] = i;
                    emptiesC[emptyCount] = j;
                    emptyCount++;
                } else {
                    int bit = 1 << v;
                    rowMask[i] |= bit;
                    colMask[j] |= bit;
                    boxMask[(i / 3) * 3 + (j / 3)] |= bit;
                }
            }
        }

        dfs(0);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(board[i][j]);
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }

    static boolean dfs(int idx) {
        if (idx == emptyCount) {
            return true;
        }

        int r = emptiesR[idx];
        int c = emptiesC[idx];
        int box = (r / 3) * 3 + (c / 3);

        int used = rowMask[r] | colMask[c] | boxMask[box];
        int bits = (~used) & FULL;

        while (bits != 0) {
            int bit = bits & -bits;
            bits -= bit;

            int v = Integer.numberOfTrailingZeros(bit);

            board[r][c] = v;
            rowMask[r] |= bit;
            colMask[c] |= bit;
            boxMask[box] |= bit;

            if (dfs(idx + 1)) {
                return true;
            }

            board[r][c] = 0;
            rowMask[r] ^= bit;
            colMask[c] ^= bit;
            boxMask[box] ^= bit;
        }

        return false;
    }
}