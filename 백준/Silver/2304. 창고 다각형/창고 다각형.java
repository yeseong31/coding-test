import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

class Point {
    final int l;
    final int h;

    Point(int l, int h) {
        this.l = l;
        this.h = h;
    }
}

public class Main {
    static FastReader sc = new FastReader();
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        input();
        System.out.println(sb);
    }

    static void input() {
        int n = sc.nextInt();
        Point[] points = new Point[n];

        int maxH = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            int l = sc.nextInt();
            int h = sc.nextInt();

            points[i] = new Point(l, h);
            maxH = Math.max(maxH, h);
        }
        Arrays.sort(points, (p1, p2) -> p1.l - p2.l);

        int area = 0;

        int prevL = points[0].l;
        int prevH = -1;

        int leftPointL = Integer.MAX_VALUE;
        int rightPointL = Integer.MIN_VALUE;

        // 왼쪽부터
        for (int i = 0; i < n; i++) {
            int currentL = points[i].l;
            int currentH = points[i].h;

            if (prevH < currentH) {
                if (prevH > 0) {
                    area += (currentL - prevL) * prevH;
                }
                prevL = currentL;
                prevH = currentH;
            }

            if (currentH == maxH) {
                leftPointL = points[i].l;
                break;
            };
        }

        prevL = points[n - 1].l;
        prevH = -1;

        for (int i = n - 1; i >= 0; i--) {
            int currentL = points[i].l;
            int currentH = points[i].h;

            if (prevH < currentH) {
                if (prevH > 0) {
                    area += (prevL - currentL) * prevH;
                }
                prevL = currentL;
                prevH = currentH;
            }

            if (currentH == maxH) {
                rightPointL = points[i].l;
                break;
            };
        }

        area += (rightPointL - leftPointL + 1) * maxH;
        sb.append(area);
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}