import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        long[] numbers = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            numbers[i] = Long.parseLong(br.readLine());
        }

        SegTree segTree = new SegTree(n + 1);
        segTree.init(numbers);

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            long minValue = segTree.queryMin(a, b);

            sb.append(minValue).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static class SegTree {
        private final int N;
        private final long[] arr;
        private final long[] minSeg;

        SegTree(int n) {
            N = n;
            arr = new long[N];
            minSeg = new long[N * 4];
        }

        private void setArray(long[] data) {
            if (data.length != N) {
                throw new IllegalArgumentException();
            }
            System.arraycopy(data, 0, arr, 0, N);
        }

        private void init(int node, int src, int dst) {
            if (src == dst) {
                minSeg[node] = arr[src];
                return;
            }

            int mid = (src + dst) >> 1;
            init(node << 1, src, mid);
            init((node << 1) | 1, mid + 1, dst);

            minSeg[node] = Math.min(minSeg[node << 1], minSeg[(node << 1) | 1]);
        }

        public void init(long[] data) {
            setArray(data);
            init(1, 0, N - 1);
        }

        private void update(int node, int src, int dst, int idx, long value) {
            if (idx < src || dst < idx) return;
            if (src == dst) {
                minSeg[node] = value;
                return;
            }

            int mid = (src + dst) >> 1;
            update(node << 1, src, mid, idx, value);
            update((node << 1) | 1, mid + 1, dst, idx, value);

            minSeg[node] = Math.min(minSeg[node << 1], minSeg[(node << 1) | 1]);
        }

        private long queryMin(int node, int src, int dst, int left, int right) {
            if (dst < left || right < src) return Long.MAX_VALUE;
            if (left <= src && dst <= right) return minSeg[node];

            int mid = (src + dst) >> 1;
            return Math.min(
                    queryMin(node << 1, src, mid, left, right),
                    queryMin((node << 1) | 1, mid + 1, dst, left, right));
        }

        public long queryMin(int left, int right) {
            if (left < 0) left = 0;
            if (right >= N) right = N - 1;
            if (left > right) return Long.MAX_VALUE;

            return queryMin(1, 0, N - 1, left, right);
        }
    }
}