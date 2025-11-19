import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static final List<int[]> edges = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            edges.add(new int[]{u, v, t});
        }

        int[] parents = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parents[i] = i;
        }

        edges.sort((a, b) -> Integer.compare(a[2], b[2]));

        int day = 1;  // 날짜(d)
        int cnt = 0;  // 연결된 학윈 수(union 수)

        for (int[] e : edges) {
            int u = e[0];
            int v = e[1];
            int t = e[2];

            if (t > day) {
                break;
            }

            if (find(parents, u) != find(parents, v)) {
                union(parents, u, v);
                day++;
                if (++cnt == n - 1) {
                    break;
                }
            }
        }

        System.out.println(day);
    }

    private static int find(int[] parents, int x) {
        if (parents[x] != x) {
            parents[x] = find(parents, parents[x]);
        }
        return parents[x];
    }

    private static void union(int[] parents, int a, int b) {
        a = find(parents, a);
        b = find(parents, b);
        if (a < b) {
            parents[b] = a;
        } else {
            parents[a] = b;
        }
    }
}