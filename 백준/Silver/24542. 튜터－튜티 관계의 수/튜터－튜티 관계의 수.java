import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    private static final int MOD = 1_000_000_007;

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

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] parents = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parents[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            if (find(parents, u) != find(parents, v)) {
                union(parents, u, v);
            }
        }

        for (int i = 0; i <= n; i++) {
            parents[i] = find(parents, i);
        }

        Map<Integer, Integer> countMap = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            int key = parents[i];
            countMap.put(key, countMap.getOrDefault(key, 0) + 1);
        }

        int answer = 1;
        for (int value : countMap.values()) {
            answer = (int) (((long) answer * value) % MOD);
        }

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}