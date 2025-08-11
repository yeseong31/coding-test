import java.io.*;
import java.util.*;

public class Main {

    private static int[] solution(int n, int m, int k, int t, int[][] points) {
        int maxCount = 0;
        int ansX = 0;
        int ansY = 0;

        for (int i = 0; i < t; i++) {
            int lx = points[i][0];
            int rx = lx + k;

            if (rx > n) {
                lx -= (rx - n);
                rx = n;
                if (lx < 0) lx = 0;
            }

            for (int j = 0; j < t; j++) {
                int ry = points[j][1];
                int ly = ry - k;

                if (ly < 0) {
                    ly = 0;
                    ry = k;
                }

                int count = 0;
                for (int p = 0; p < t; p++) {
                    int px = points[p][0];
                    int py = points[p][1];
                    if (lx <= px && px <= rx && ly <= py && py <= ry) count++;
                }

                if (count > maxCount) {
                    maxCount = count;
                    ansX = lx;
                    ansY = ry;
                }
            }
        }

        return new int[]{ansX, ansY, maxCount};
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] points = new int[t][2];
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            points[i][0] = Integer.parseInt(st.nextToken());
            points[i][1] = Integer.parseInt(st.nextToken());
        }

        int[] answer = solution(n, m, k, t, points);
        sb.append(answer[0]).append(" ").append(answer[1]).append("\n").append(answer[2]);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
