import java.io.*;
import java.util.*;

public class Main {

    private static final Set<List<Integer>> combinations = new HashSet<>();
    private static final List<Integer> result = new ArrayList<>();
    private static final StringBuilder sb = new StringBuilder();

    private static int n, m;
    private static int[] arr;
    private static boolean[] visited;

    private static void dfs(int depth) {
        if (depth == m) {
            if (!combinations.contains(result)) {
                combinations.add(result);
                for (int num : result) {
                    sb.append(num).append(" ");
                }
                sb.append("\n");
            }
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;

            visited[i] = true;
            result.add(arr[i]);

            dfs(depth + 1);

            visited[i] = false;
            result.remove(result.size() - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        visited = new boolean[n];

        dfs(0);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
