import java.util.*;

class Solution {
    
    public String solution(int n, int t, int m, String[] timetable) {
        
        List<Integer> crews = new ArrayList<>();
        for (String time : timetable) {
            int hour = Integer.parseInt(time.substring(0, 2));
            int minute = Integer.parseInt(time.substring(3, 5));
            crews.add(hour * 60 + minute);
        }

        crews.sort(Collections.reverseOrder());

        List<int[]> answer = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int departTime = 9 * 60 + i * t;
            int cnt = 0;
            int prev = departTime;

            while (!crews.isEmpty() && cnt < m && crews.get(crews.size() - 1) <= departTime) {
                prev = crews.remove(crews.size() - 1);
                cnt++;
            }

            answer.add(new int[]{departTime, cnt, prev});
        }

        int target;
        int[] last = answer.get(answer.size() - 1);

        if (last[1] < m) {
            target = last[0];
        } else {
            target = last[2] - 1;
        }

        int hour = target / 60;
        int minute = target % 60;

        return String.format("%02d:%02d", hour, minute);
    }
}