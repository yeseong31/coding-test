import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

class Solution {

    private static final DateTimeFormatter FORMATTER = DateTimeFormatter.ofPattern("HHmm");

    private String convertTime(int time) {
        String timeStr = String.format("%04d", time);
        LocalTime targetTime = LocalTime.parse(timeStr, FORMATTER);
        return targetTime.format(FORMATTER);
    }

    private String getDeadlineTime(String timeStr) {
        LocalTime deadline = LocalTime.parse(timeStr, FORMATTER).plusMinutes(10);
        return deadline.format(FORMATTER);
    }

    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        startday -= 1;

        for (int i = 0; i < schedules.length; i++) {
            String scheduleTime = convertTime(schedules[i]);
            String deadline = getDeadlineTime(scheduleTime);

            int count = 0;
            int[] timelog = timelogs[i];

            for (int j = 0; j < timelog.length; j++) {
                int day = (startday + j) % 7;
                
                if (day >= 5) {
                    continue;
                }

                String logTime = convertTime(timelog[j]);
                if (logTime.compareTo(deadline) <= 0) {
                    count++;
                }
            }

            if (count == 5) {
                answer++;
            }
        }

        return answer;
    }
}