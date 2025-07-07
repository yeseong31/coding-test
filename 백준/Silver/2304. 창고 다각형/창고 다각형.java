import java.io.*;
import java.util.Arrays;

class Point {
    final int l;
    final int h;

    Point(int l, int h) {
        this.l = l;
        this.h = h;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int answer = 0;

        int n = Integer.parseInt(br.readLine());
        Point[] points = new Point[n];

        int maxH = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            int l = Integer.parseInt(input[0]);
            int h = Integer.parseInt(input[1]);

            points[i] = new Point(l, h);
            maxH = Math.max(maxH, h);
        }
        
        Arrays.sort(points, (p1, p2) -> p1.l - p2.l);

        int prevL = points[0].l;
        int prevH = -1;

        int leftPointL = Integer.MAX_VALUE;
        int rightPointL = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            int currentL = points[i].l;
            int currentH = points[i].h;

            if (prevH < currentH) {
                if (prevH > 0) {
                    answer += (currentL - prevL) * prevH;
                }
                prevL = currentL;
                prevH = currentH;
            }

            if (currentH == maxH) {
                leftPointL = points[i].l;
                break;
            }
            ;
        }

        prevL = points[n - 1].l;
        prevH = -1;

        for (int i = n - 1; i >= 0; i--) {
            int currentL = points[i].l;
            int currentH = points[i].h;

            if (prevH < currentH) {
                if (prevH > 0) {
                    answer += (prevL - currentL) * prevH;
                }
                prevL = currentL;
                prevH = currentH;
            }

            if (currentH == maxH) {
                rightPointL = points[i].l;
                break;
            }
            ;
        }

        answer += (rightPointL - leftPointL + 1) * maxH;

        bw.write(answer + "");
        bw.flush();

    }
}