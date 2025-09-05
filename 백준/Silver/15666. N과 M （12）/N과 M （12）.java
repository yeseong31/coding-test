import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static final List<Integer> numbers = new ArrayList<>();
    private static final boolean[] visited = new boolean[10_001];
    private static final StringBuilder sb = new StringBuilder();

    private static int n;
    private static int m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());

            if (!visited[x]) {
                visited[x] = true;
                numbers.add(x);
            }
        }

        Collections.sort(numbers);
        dfs(0, 0, new ArrayList<>());

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    private static void dfs(int start, int depth, List<Integer> result) {
        if (depth == m) {
            for (int i = 0; i < m; i++) {
                sb.append(result.get(i)).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = start; i < numbers.size(); i++) {
            result.add(numbers.get(i));
            dfs(i, depth + 1, result);
            result.remove(depth);
        }
    }
}