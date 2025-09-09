import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        boolean[] known = new boolean[n + 1];
        int[] parents = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parents[i] = i;
        }

        st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());

        for (int i = 0; i < k; i++) {
            known[Integer.parseInt(st.nextToken())] = true;
        }

        int[] partyParents = new int[m];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int persons = Integer.parseInt(st.nextToken());

            int prev = Integer.parseInt(st.nextToken());

            for (int j = 1; j < persons; j++) {
                int curr = Integer.parseInt(st.nextToken());
                if (find(parents, prev) != find(parents, curr)) {
                    union(parents, prev, curr, known);
                }
                prev = parents[prev];
            }

            partyParents[i] = prev;
        }

        for (int i = 1; i <= n; i++) {
            parents[i] = find(parents, i);
            if (known[parents[i]]) known[i] = true;
        }

        int answer = 0;
        for (int i = 0; i < m; i++) {
            if (!known[partyParents[i]]) answer++;
        }

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int find(int[] parents, int x) {
        if (parents[x] != x) {
            parents[x] = find(parents, parents[x]);
        }
        return parents[x];
    }

    private static void union(int[] parents, int a, int b, boolean[] known) {
        a = find(parents, a);
        b = find(parents, b);

        if (known[a]) {
            parents[b] = a;
        } else {
            parents[a] = b;
        }
    }
}