import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int solution(int[][] ladders, int[][] snakes) {
        int[] arr = new int[101];
        boolean[] visited = new boolean[101];

        for (int[] ladder : ladders) arr[ladder[0]] = ladder[1];
        for (int[] snake : snakes) arr[snake[0]] = snake[1];

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{1, 0});
        visited[1] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int number = current[0];
            int step = current[1];

            if (number == 100) return step;

            for (int i = 1; i <= 6; i++) {
                int next = number + i;

                if (next > 100) continue;

                if (arr[next] != 0) {
                    next = arr[next];
                }
                if (!visited[next]) {
                    visited[next] = true;
                    queue.offer(new int[]{next, step + 1});
                }
            }
        }

        return arr[100];
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] ladders = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            ladders[i][0] = Integer.parseInt(st.nextToken());
            ladders[i][1] = Integer.parseInt(st.nextToken());
        }

        int[][] snakes = new int[m][2];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            snakes[i][0] = Integer.parseInt(st.nextToken());
            snakes[i][1] = Integer.parseInt(st.nextToken());
        }

        int answer = solution(ladders, snakes);
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}