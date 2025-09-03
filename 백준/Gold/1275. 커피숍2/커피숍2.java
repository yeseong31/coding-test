import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        long[] numbers = new long[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = Long.parseLong(st.nextToken());
        }

        SegTree segTree = new SegTree(n);
        segTree.init(numbers);

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken());

            long result = segTree.query(Math.min(x, y), Math.max(x, y));
            sb.append(result).append("\n");

            segTree.set(a, b);
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
    
    private static class SegTree {
        private final int N;
        private final long[] arr;
        private final long[] seg;
        private final long[] lazy;

        SegTree(int n) {
            N = n;
            arr = new long[N];
            seg = new long[N * 4];
            lazy = new long[N * 4];
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

        public void init(long[] numbers) {
            setArray(numbers);
            init(1, 0, N - 1);
        }

        private void apply(int node, int src, int dst, long value) {
            seg[node] += value * (dst - src + 1);
            lazy[node] += value;
        }

        private void push(int node, int src, int dst) {
            if (lazy[node] == 0L || src == dst) return;

            int mid = (src + dst) >> 1;
            long add = lazy[node];

            apply(node << 1, src, mid, add);
            apply((node << 1) | 1, mid + 1, dst, add);

            lazy[node] = 0L;
        }

        private void rangeAdd(int node, int src, int dst, int left, int right, long value) {
            if (dst < left || right < src) return;
            if (left <= src && dst <= right) {
                apply(node, src, dst, value);
                return;
            }

            push(node, src, dst);

            int mid = (src + dst) >> 1;
            rangeAdd(node << 1, src, mid, left, right, value);
            rangeAdd((node << 1) | 1, mid + 1, dst, left, right, value);

            seg[node] = seg[node << 1] + seg[(node << 1) | 1];
        }

        public void rangeAdd(int left, int right, long value) {
            if (left < 0) left = 0;
            if (right >= N) right = N - 1;
            if (left > right) return;

            rangeAdd(1, 0, N - 1, left, right, value);
        }

        private long query(int node, int src, int dst, int left, int right) {
            if (dst < left || right < src) return 0L;
            if (left <= src && dst <= right) return seg[node];

            push(node, src, dst);

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
            if (idx < 0 || idx >= N) return;

            long curr = query(idx, idx);
            long diff = value - curr;

            arr[idx] = value;
            rangeAdd(idx, idx, diff);
        }

        public void add(int idx, long value) {
            if (idx < 0 || idx >= N) return;

            arr[idx] += value;
            rangeAdd(idx, idx, value);
        }
    }
}