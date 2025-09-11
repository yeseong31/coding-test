import java.io.*;
import java.util.*;

public class Solution {

    private static final int LIMIT = 3;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            int n = Integer.parseInt(br.readLine());

            List<Point> persons = new ArrayList<>();
            List<Point> stairs = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());

                for (int j = 0; j < n; j++) {
                    int x = Integer.parseInt(st.nextToken());
                    if (x == 1) persons.add(new Point(i, j));
                    if (x > 1) stairs.add(new Point(i, j, x));
                }
            }

            int answer = Integer.MAX_VALUE;
            for (int choice = 0; choice < (1 << persons.size()); choice++) {
                answer = Math.min(answer, simulation(choice, persons, stairs));
            }

            sb.append("#")
                    .append(testCase)
                    .append(" ")
                    .append(answer)
                    .append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    private static int simulation(int choice, List<Point> persons, List<Point> stairs) {
        List<Integer> useA = new ArrayList<>();
        List<Integer> useB = new ArrayList<>();

        for (int i = 0; i < persons.size(); i++) {
            Point p = persons.get(i);
            Point s;
            int dist;

            if ((choice & (1 << i)) == 0) {
                s = stairs.get(0);
                dist = getDist(p.x, p.y, s.x, s.y);
                useA.add(dist);
            } else {
                s = stairs.get(1);
                dist = getDist(p.x, p.y, s.x, s.y);
                useB.add(dist);
            }
        }

        int lengthA = stairs.get(0).length;
        int lengthB = stairs.get(1).length;

        int timeA = measureTime(useA, lengthA);
        int timeB = measureTime(useB, lengthB);

        return Math.max(timeA, timeB);
    }

    private static int measureTime(List<Integer> waitingList, int stairsLength) {
        if (waitingList.isEmpty()) return 0;

        Collections.sort(waitingList);
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int answer = 0;

        for (int a : waitingList) {
            int t = a + 1;

            while (!pq.isEmpty() && pq.peek() <= t) {
                pq.poll();
            }

            if (pq.size() >= LIMIT) {
                t = pq.poll();
                while (!pq.isEmpty() && pq.peek() <= t) {
                    pq.poll();
                }
            }

            int outTime = t + stairsLength;
            pq.add(outTime);
            answer = Math.max(answer, outTime);
        }

        return answer;
    }

    private static int getDist(int x, int y, int ox, int oy) {
        return Math.abs(x - ox) + Math.abs(y - oy);
    }

    private static class Point {
        final int x;
        final int y;
        final int length;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
            this.length = 0;
        }

        Point(int x, int y, int length) {
            this.x = x;
            this.y = y;
            this.length = length;
        }
    }
}