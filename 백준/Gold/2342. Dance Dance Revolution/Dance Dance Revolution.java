import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] cost = buildCost();
        int[] curr = new int[25];
        int[] next = new int[25];

        Arrays.fill(curr, INF);
        curr[idx(0, 0)] = 0;

        String line;
        while ((line = br.readLine()) != null) {
            if (line.isEmpty()) {
                continue;
            }
            StringTokenizer st = new StringTokenizer(line);
            while (st.hasMoreTokens()) {
                int p = Integer.parseInt(st.nextToken());
                if (p == 0) {
                    int answer = INF;
                    for (int s = 0; s < 25; s++) {
                        answer = Math.min(answer, curr[s]);
                    }
                    System.out.println(answer);
                    return;
                }

                Arrays.fill(next, INF);

                for (int s = 0; s < 25; s++) {
                    int base = curr[s];
                    if (base == INF) {
                        continue;
                    }

                    int l = s / 5;
                    int r = s % 5;

                    int s1 = idx(p, r);
                    int v1 = base + cost[l * 5 + p];
                    if (v1 < next[s1]) {
                        next[s1] = v1;
                    }

                    int s2 = idx(l, p);
                    int v2 = base + cost[r * 5 + p];
                    if (v2 < next[s2]) {
                        next[s2] = v2;
                    }
                }

                int[] tmp = curr;
                curr = next;
                next = tmp;
            }
        }
    }

    private static int idx(int l, int r) {
        return l * 5 + r;
    }

    private static int[] buildCost() {
        int[] c = new int[25];

        for (int prev = 0; prev < 5; prev++) {
            for (int next = 0; next < 5; next++) {
                int v;
                if (prev == 0) {
                    v = 2;
                } else if (prev == next) {
                    v = 1;
                } else if (Math.abs(next - prev) == 2) {
                    v = 4;
                } else {
                    v = 3;
                }
                c[prev * 5 + next] = v;
            }
        }

        return c;
    }
}