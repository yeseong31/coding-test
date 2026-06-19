class Solution {

    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        startday -= 1;

        for (int i = 0; i < schedules.length; i++) {
            int deadline = toMinutes(schedules[i]) + 10;
            int[] timelog = timelogs[i];

            int onTimeCount = 0;
            for (int j = 0; j < timelog.length; j++) {
                int day = (startday + j) % 7;
                if (day >= 5) continue;

                if (toMinutes(timelog[j]) <= deadline) {
                    onTimeCount++;
                }
            }

            if (onTimeCount == 5) {
                answer++;
            }
        }

        return answer;
    }

    private int toMinutes(int hhmm) {
        return (hhmm / 100) * 60 + (hhmm % 100);
    }
}