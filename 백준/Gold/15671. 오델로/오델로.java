import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    private static final int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    private static final int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};

    private static final int SIZE = 6;
    private static final char BLACK = 'B';
    private static final char WHITE = 'W';

    private static boolean isInside(int x, int y) {
        return x >= 0 && x < SIZE && y >= 0 && y < SIZE;
    }

    private static int flipStones(int x, int y, char c, char[][] board) {
        int flipped = 0;

        for (int d = 0; d < 8; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            int count = 0;
            while (isInside(nx, ny) && board[nx][ny] != '.' && board[nx][ny] != c) {
                count++;
                nx += dx[d];
                ny += dy[d];
            }

            if (isInside(nx, ny) && board[nx][ny] == c && count > 0) {
                int bx = x + dx[d];
                int by = y + dy[d];

                for (int i = 0; i < count; i++) {
                    board[bx][by] = c;
                    flipped++;
                    bx += dx[d];
                    by += dy[d];
                }
            }
        }

        return flipped;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        char[][] board = new char[SIZE][SIZE];
        for (char[] row : board) {
            Arrays.fill(row, '.');
        }

        board[2][2] = WHITE;
        board[3][3] = WHITE;
        board[2][3] = BLACK;
        board[3][2] = BLACK;

        int prev = -1;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            char c = (i % 2 == 0) ? BLACK : WHITE;

            board[x][y] = c;

            int curr = flipStones(x, y, c, board);
            if (prev == 0 && curr == 0) break;
            prev = curr;
        }

        Map<Character, Integer> countMap = new HashMap<>();
        for (int x = 0; x < SIZE; x++) {
            for (int y = 0; y < SIZE; y++) {
                countMap.put(board[x][y], countMap.getOrDefault(board[x][y], 0) + 1);
            }
        }

        for (char[] row : board) {
            sb.append(new String(row)).append('\n');
        }

        if (countMap.getOrDefault(BLACK, 0) >= countMap.getOrDefault(WHITE, 0)) {
            sb.append("Black");
        } else {
            sb.append("White");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}