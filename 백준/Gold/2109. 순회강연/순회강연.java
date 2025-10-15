import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] lectures = new int[n][2];

        int maxDay = 0;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            lectures[i][0] = Integer.parseInt(st.nextToken());
            lectures[i][1] = Integer.parseInt(st.nextToken());
            maxDay = Math.max(maxDay, lectures[i][1]);
        }

        Arrays.sort(lectures, (a, b) -> b[1] - a[1]);
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        int idx = 0;
        int answer = 0;

        for (int day = maxDay; day >= 1; day--) {
            while (idx < n && lectures[idx][1] >= day) {
                pq.offer(lectures[idx++][0]);
            }
            if (!pq.isEmpty()) answer += pq.poll();
        }

        System.out.println(answer);
    }
}