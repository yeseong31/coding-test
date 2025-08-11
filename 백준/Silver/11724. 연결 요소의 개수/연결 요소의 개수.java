import java.io.*;
import java.util.*;

public class Main {

    private static int findParents(int[] parents, int x) {
        if (parents[x] != x) {
            parents[x] = findParents(parents, parents[x]);
        }
        return parents[x];
    }

    private static void unionParents(int[] parents, int a, int b) {
        a = findParents(parents, a);
        b = findParents(parents, b);

        if (a < b) {
            parents[b] = a;
        } else {
            parents[a] = b;
        }
    }

    private static int solution(int n, List<List<Integer>> graph) {
        int[] parents = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parents[i] = i;
        }

        for (int curr = 1; curr <= n; curr++) {
            for (int next : graph.get(curr)) {
                if (findParents(parents, curr) != findParents(parents, next)) {
                    unionParents(parents, curr, next);
                }
            }
        }

        Set<Integer> count = new HashSet<>();
        for (int i = 1; i <= n; i++) {
            count.add(findParents(parents, i));
        }

        return count.size();
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        int answer = solution(n, graph);
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

}
