import java.io.*;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static final int LIMIT = 200_001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] answer = solution(n, k);
        sb.append(answer[0]).append("\n").append(answer[1]);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int[] solution(int n, int k) {
        int minDist = Integer.MAX_VALUE;
        int count = 0;

        int[] distances = new int[LIMIT];
        Arrays.fill(distances, Integer.MAX_VALUE);
        distances[n] = 0;

        Queue<Integer> queue = new LinkedList<>();
        queue.add(n);

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            int step = distances[curr];

            if (step > minDist) continue;

            if (curr == k) {
                if (minDist == step) {
                    count++;
                } else {
                    minDist = step;
                    count = 1;
                }
                continue;
            }

            int[] nextPositions = {curr - 1, curr + 1, curr * 2};

            for (int next : nextPositions) {
                if (next >= 0 && next < LIMIT) {
                    if (distances[next] >= step + 1) {
                        distances[next] = step + 1;
                        queue.offer(next);
                    }
                }
            }
        }

        return new int[]{minDist, count};
    }
}
