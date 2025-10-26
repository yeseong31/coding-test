import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    private static int answer;
    private static int N;
    private static int K;
    private static int[][] times;
    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        times = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                times[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        answer = Integer.MAX_VALUE;
        visited = new boolean[N];
        visited[K] = true;

        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    times[i][j] = Math.min(times[i][j], times[i][k] + times[k][j]);
                }
            }
        }

        findMin(K, 0, 1);

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static void findMin(int curr, int cost, int count) {
        if (count == N) {
            answer = Math.min(answer, cost);
            return;
        }

        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                findMin(i, cost + times[curr][i], count + 1);
                visited[i] = false;
            }
        }
    }
}