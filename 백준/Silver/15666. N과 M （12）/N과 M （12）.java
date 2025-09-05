import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    private static final List<Integer> numbers = new ArrayList<>();
    private static final boolean[] visited = new boolean[10_001];

    private static int n;
    private static int m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
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

        br.close();
    }

    private static void dfs(int start, int depth, List<Integer> result) {
        if (depth == m) {
            System.out.println(result.stream()
                    .map(String::valueOf)
                    .collect(Collectors.joining(" ")));
            return;
        }

        for (int i = start; i < numbers.size(); i++) {
            result.add(numbers.get(i));
            dfs(i, depth + 1, result);
            result.remove(result.size() - 1);
        }
    }
}