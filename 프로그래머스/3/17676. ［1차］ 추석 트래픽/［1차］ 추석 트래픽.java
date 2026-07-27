import java.util.*;

class Solution {

    public int solution(String[] lines) {
        int n = lines.length;
        double[] starts = new double[n];
        double[] ends = new double[n];

        for (int i = 0; i < n; i++) {
            String[] parts = lines[i].split(" ");
            String[] t = parts[1].split(":");
            double s = Double.parseDouble(parts[2].replace("s", ""));
            double end = (Integer.parseInt(t[0]) * 3600
                       + Integer.parseInt(t[1]) * 60
                       + Double.parseDouble(t[2])) * 1000;
            double start = end - s * 1000 + 1;
            starts[i] = start;
            ends[i] = end;
        }

        int answer = 0;
        for (int i = 0; i < n; i++) {
            answer = Math.max(answer, check(starts[i], starts, ends, n));
            answer = Math.max(answer, check(ends[i], starts, ends, n));
        }
        return answer;
    }

    private int check(double startTime, double[] starts, double[] ends, int n) {
        double endTime = startTime + 1000;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (starts[i] < endTime && ends[i] >= startTime) count++;
        }
        return count;
    }
}