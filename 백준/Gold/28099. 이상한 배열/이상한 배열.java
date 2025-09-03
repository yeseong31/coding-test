import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    private static final Set<Integer> checked = new HashSet<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());

            int[] numbers = new int[n + 1];
            int[] minIndices = new int[n + 1];
            int[] maxIndices = new int[n + 1];

            Arrays.fill(minIndices, Integer.MAX_VALUE);
            Arrays.fill(maxIndices, Integer.MIN_VALUE);
            checked.clear();

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int a = Integer.parseInt(st.nextToken());

                minIndices[a] = Math.min(minIndices[a], j);
                maxIndices[a] = Math.max(maxIndices[a], j);

                numbers[j] = a;
                checked.add(a);
            }

            SegTree segTree = new SegTree(n + 1);
            segTree.init(numbers);

            boolean answer = true;

            for (int x : checked) {
                int left = minIndices[x];
                int right = maxIndices[x];

                if (left == Integer.MAX_VALUE) continue;
                if (right == Integer.MIN_VALUE) continue;

                int result = segTree.queryMax(left, right);
                if (result > x) {
                    answer = false;
                    break;
                }
            }

            sb.append(answer ? "Yes" : "No").append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static class SegTree {
        private final int N;
        private final int[] arr;
        private final int[] maxSeg;

        SegTree(int n) {
            N = n;
            arr = new int[N];
            maxSeg = new int[n * 4];
        }

        private void setArray(int[] data) {
            if (data.length != N) {
                throw new IllegalArgumentException();
            }
            System.arraycopy(data, 0, arr, 0, N);
        }

        private void init(int node, int src, int dst) {
            if (src == dst) {
                maxSeg[node] = arr[src];
                return;
            }

            int mid = (src + dst) >> 1;
            init(node << 1, src, mid);
            init((node << 1) | 1, mid + 1, dst);

            maxSeg[node] = Math.max(maxSeg[node << 1], maxSeg[(node << 1) | 1]);
        }

        public void init(int[] data) {
            setArray(data);
            init(1, 0, N - 1);
        }

        private void update(int node, int src, int dst, int idx, int val) {
            if (idx < src || idx > dst) return;
            if (src == dst) {
                maxSeg[node] = val;
                return;
            }

            int mid = (src + dst) >> 1;
            update(node << 1, src, mid, idx, val);
            update((node << 1) | 1, mid + 1, dst, idx, val);

            maxSeg[node] = Math.max(maxSeg[node << 1], maxSeg[(node << 1) | 1]);
        }

        private int queryMax(int node, int src, int dst, int left, int right) {
            if (dst < left || right < src) return Integer.MIN_VALUE;
            if (left <= src && dst <= right) return maxSeg[node];

            int mid = (src + dst) >> 1;
            return Math.max(
                    queryMax(node << 1, src, mid, left, right),
                    queryMax((node << 1) | 1, mid + 1, dst, left, right));
        }

        public int queryMax(int left, int right) {
            if (left < 0) left = 0;
            if (right >= N) right = N - 1;
            if (left > right) return Integer.MIN_VALUE;

            return queryMax(1, 0, N - 1, left, right);
        }
    }
}