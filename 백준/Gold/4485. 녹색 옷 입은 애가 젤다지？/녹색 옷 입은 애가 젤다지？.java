import java.io.*;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    static final int[] dx = {1, 0, -1, 0};
    static final int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int cnt = 1;

        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) {
                break;
            }

            int[][] board = new int[n][n];
            for (int i = 0; i < n; i++) {
                String[] line = br.readLine().split(" ");
                for (int j = 0; j < n; j++) {
                    board[i][j] = Integer.parseInt(line[j]);
                }
            }

            sb.append("Problem ")
                    .append(cnt++)
                    .append(": ")
                    .append(solution(n, board))
                    .append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    public static int solution(int n, int[][] board) {
        int[][] check = new int[n][n];
        PriorityQueue<Node> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            Arrays.fill(check[i], Integer.MAX_VALUE);
        }

        int x = 0;
        int y = 0;

        check[x][y] = board[x][y];
        pq.offer(new Node(x, y, board[x][y]));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            x = current.x;
            y = current.y;

            if (current.cost > check[x][y]) continue;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                    continue;
                }

                int newCost = check[x][y] + board[nx][ny];
                if (check[nx][ny] > newCost) {
                    check[nx][ny] = newCost;
                    pq.offer(new Node(nx, ny, newCost));
                }
            }
        }

        return check[n - 1][n - 1];
    }

    static class Node implements Comparable<Node> {
        final int x;
        final int y;
        final int cost;

        public Node(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.cost, other.cost);
        }
    }
}