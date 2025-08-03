import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    private static class Node implements Comparable<Node> {
        public final int x;
        public final int y;
        public final int c;

        public Node(int x, int y, int c) {
            this.x = x;
            this.y = y;
            this.c = c;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.c, other.c);
        }
    }

    private static int bfs01(int n, int m, List<List<List<Node>>> graph) {
        int[][] dist = new int[n + 1][m + 1];
        for (int[] row : dist) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }

        Deque<Node> deque = new ArrayDeque<>();
        deque.offerFirst(new Node(0, 0, 0));
        dist[0][0] = 0;

        while (!deque.isEmpty()) {
            Node current = deque.pollFirst();
            int x = current.x;
            int y = current.y;
            int c = current.c;

            if (x == n && y == m) return c;

            for (Node next : graph.get(x).get(y)) {
                int nx = next.x;
                int ny = next.y;
                int nc = next.c;

                if (dist[nx][ny] > c + nc) {
                    dist[nx][ny] = c + nc;

                    if (nc == 0) {
                        deque.offerFirst(new Node(nx, ny, c + nc));
                    } else {
                        deque.offerLast(new Node(nx, ny, c + nc));
                    }
                }
            }
        }

        return -1;
    }

    private static int solution(int n, int m, char[][] board) {
        List<List<List<Node>>> graph = new ArrayList<>();

        for (int i = 0; i <= n; i++) {
            List<List<Node>> row = new ArrayList<>();

            for (int j = 0; j <= m; j++) {
                row.add(new ArrayList<>());
            }

            graph.add(row);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == '/') {
                    graph.get(i).get(j + 1).add(new Node(i + 1, j, 0));
                    graph.get(i + 1).get(j).add(new Node(i, j + 1, 0));
                    graph.get(i).get(j).add(new Node(i + 1, j + 1, 1));
                    graph.get(i + 1).get(j + 1).add(new Node(i, j, 1));
                } else {
                    graph.get(i).get(j).add(new Node(i + 1, j + 1, 0));
                    graph.get(i + 1).get(j + 1).add(new Node(i, j, 0));
                    graph.get(i).get(j + 1).add(new Node(i + 1, j, 1));
                    graph.get(i + 1).get(j).add(new Node(i, j + 1, 1));
                }
            }
        }

        return bfs01(n, m, graph);
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[][] board = new char[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            char[] row = st.nextToken().toCharArray();

            for (int j = 0; j < m; j++) {
                board[i][j] = row[j];
            }
        }

        int answer = solution(n, m, board);
        sb.append(answer >= 0 ? answer : "NO SOLUTION");

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}