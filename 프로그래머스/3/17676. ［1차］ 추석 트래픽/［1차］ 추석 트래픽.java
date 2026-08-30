import java.math.BigDecimal;
import java.time.LocalTime;

class Solution {

    private static final long WINDOW_SIZE = 1_000L;

    public int solution(String[] lines) {
        int n = lines.length;
        long[] starts = new long[n];
        long[] ends = new long[n];

        for (int i = 0; i < n; i++) {
            String[] parts = lines[i].split(" ");

            long end = parseTime(parts[1]);
            long duration = parseDuration(parts[2]);

            ends[i] = end;
            starts[i] = end - duration + 1;
        }

        int answer = 0;

        for (long windowStart : ends) {
            long windowEnd = windowStart + WINDOW_SIZE - 1;
            int count = 0;

            for (int i = 0; i < n; i++) {
                if (starts[i] <= windowEnd && ends[i] >= windowStart) {
                    count++;
                }
            }

            answer = Math.max(answer, count);
        }

        return answer;
    }

    private long parseTime(String time) {
        return LocalTime.parse(time).toNanoOfDay() / 1_000_000;
    }

    private long parseDuration(String duration) {
        String seconds = duration.substring(0, duration.length() - 1);

        return new BigDecimal(seconds)
                .movePointRight(3)
                .longValueExact();
    }
}