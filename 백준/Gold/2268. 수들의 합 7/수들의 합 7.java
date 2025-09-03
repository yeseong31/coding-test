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

        SegTree segTree = new SegTree(n + 1);
        segTree.init(numbers);

        for (int step = 0; step < m; step++) {
            st = new StringTokenizer(br.readLine());
            int cmd = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (cmd == 0) {
                long result = segTree.query(Math.min(a, b), Math.max(a, b));
                sb.append(result).append("\n");
            } else {
                segTree.set(a, b);
            }
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static class SegTree {
        private final int N;
        private final long[] arr;
        private final long[] seg;

        SegTree(int n) {
            N = n;
            arr = new long[N];
            seg = new long[N * 4];
        }

        private void setArray(long[] data) {
            if (data.length != N) {
                throw new IllegalArgumentException("데이터의 길이가 맞지 않습니다.");
            }
            System.arraycopy(data, 0, arr, 0, N);
        }

        private void init(int node, int src, int dst) {
            if (src == dst) {
                seg[node] = arr[src];
                return;
            }

            int mid = (src + dst) >> 1;
            init(node << 1, src, mid);
            init((node << 1) | 1, mid + 1, dst);

            seg[node] = seg[node << 1] + seg[(node << 1) | 1];
        }

        public void init(long[] data) {
            setArray(data);
            init(1, 0, N - 1);
        }

        private void update(int node, int src, int dst, int idx, long diff) {
            if (idx < src || idx > dst) return;

            seg[node] += diff;
            if (src == dst) return;

            int mid = (src + dst) >> 1;
            update(node << 1, src, mid, idx, diff);
            update((node << 1) | 1, mid + 1, dst, idx, diff);

            seg[node] = seg[node << 1] + seg[(node << 1) | 1];
        }

        private long query(int node, int src, int dst, int left, int right) {
            if (dst < left || right < src) return 0L;
            if (left <= src && dst <= right) return seg[node];

            int mid = (src + dst) >> 1;

            return query(node << 1, src, mid, left, right) + query((node << 1) | 1, mid + 1, dst, left, right);
        }

        public long query(int left, int right) {
            if (left < 0) left = 0;
            if (right >= N) right = N - 1;
            if (left > right) return 0L;

            return query(1, 0, N - 1, left, right);
        }

        public void set(int idx, long value) {
            long diff = value - arr[idx];
            arr[idx] = value;
            update(1, 0, N - 1, idx, diff);
        }
    }
}