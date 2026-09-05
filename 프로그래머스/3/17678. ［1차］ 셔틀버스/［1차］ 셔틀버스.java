import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    
    public String solution(int n, int t, int m, String[] timetable) {
        List<Integer> crews = new ArrayList<>();

        for (String time : timetable) {
            int hour = Integer.parseInt(time.substring(0, 2));
            int minute = Integer.parseInt(time.substring(3, 5));

            crews.add(hour * 60 + minute);
        }

        crews.sort(Collections.reverseOrder());

        int lastDeparture = 0;
        int lastBoardedTime = 0;
        int lastBoardedCount = 0;

        for (int bus = 0; bus < n; bus++) {
            int departure = 9 * 60 + bus * t;
            int boardedCount = 0;
            int boardedTime = 0;

            while (!crews.isEmpty()
                    && boardedCount < m
                    && crews.get(crews.size() - 1) <= departure) {

                boardedTime = crews.remove(crews.size() - 1);
                boardedCount++;
            }

            lastDeparture = departure;
            lastBoardedTime = boardedTime;
            lastBoardedCount = boardedCount;
        }

        int conTime;

        if (lastBoardedCount < m) {
            conTime = lastDeparture;
        } else {
            conTime = lastBoardedTime - 1;
        }

        return String.format(
                "%02d:%02d",
                conTime / 60,
                conTime % 60
        );
    }
}