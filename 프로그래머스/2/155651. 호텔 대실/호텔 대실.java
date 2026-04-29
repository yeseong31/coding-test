import java.util.*;

class Solution {

    private int toMinute(String time) {
        return (time.charAt(0) - '0') * 600
             + (time.charAt(1) - '0') * 60
             + (time.charAt(3) - '0') * 10
             + (time.charAt(4) - '0');
    }

    public int solution(String[][] book_time) {
        int n = book_time.length;
        int[][] times = new int[n][2];

        for (int i = 0; i < n; i++) {
            times[i][0] = toMinute(book_time[i][0]);
            times[i][1] = toMinute(book_time[i][1]) + 10;
        }

        Arrays.sort(times, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            int start = times[i][0];
            int end = times[i][1];

            if (!pq.isEmpty() && pq.peek() <= start) {
                pq.poll();
            }

            pq.offer(end);
        }

        return pq.size();
    }
}