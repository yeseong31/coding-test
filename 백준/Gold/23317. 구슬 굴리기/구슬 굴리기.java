import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        int[][] points = new int[m][2];
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            points[i][0] = x;
            points[i][1] = y;
        }

        Arrays.sort(points, (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);

        int px = 0;
        int py = 0;
        long answer = 1;

        for (int[] point : points) {
            int x = point[0];
            int y = point[1];

            int dx = x - px;
            int dy = y - py;
            
            if (dx == 0 && dy == 0) continue;
            if (dx <= 0 || dy < 0 || dy > dx) {
                System.out.println(0);
                return;
            }

            answer *= getCombination(dx, dy);
            px = x;
            py = y;
        }

        int remainingRows = n - 1 - px;
        long count = 0;

        for (int nc = py; nc < n; nc++) {
            int dc = nc - py;
            if (dc >= 0 && dc <= remainingRows) {
                count += getCombination(remainingRows, dc);
            }
        }

        answer *= count;
        System.out.println(answer);
    }

    private static long getCombination(int n, int r) {
        if (r < 0 || r > n) return 0;
        if (r == 0 || r == n) return 1;

        r = Math.min(r, n - r);
        long result = 1;

        for (int i = 0; i < r; i++) {
            result *= (n - i);
            result /= (i + 1);
            if (result < 0) return Long.MAX_VALUE;
        }

        return result;
    }
}