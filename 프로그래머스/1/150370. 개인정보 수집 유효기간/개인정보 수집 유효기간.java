import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    
    public int[] solution(String today, String[] terms, String[] privacies) {
        Map<String, Integer> periods = new HashMap<>();
        
        for (String t : terms) {
            String[] parts = t.split(" ");
            periods.put(parts[0], Integer.parseInt(parts[1]));
        }

        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < privacies.length; i++) {
            String privacy = privacies[i];
            String[] parts = privacy.split(" ");
            String dateStr = parts[0];
            String termType = parts[1];

            int[] ymd = parseDate(dateStr);
            int year = ymd[0], month = ymd[1], day = ymd[2];

            String expire = calculDate(year, month, day, periods.get(termType));
            if (expire.compareTo(today) < 0) {
                answer.add(i + 1);
            }
        }

        int[] result = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }
        Arrays.sort(result);
        return result;
    }

    private int[] parseDate(String s) {
        String[] p = s.split("\\.");
        return new int[]{Integer.parseInt(p[0]), Integer.parseInt(p[1]), Integer.parseInt(p[2])};
    }

    private String calculDate(int y, int m, int d, int p) {
        d -= 1;
        if (d == 0) {
            d = 28;
            m -= 1;
            if (m == 0) {
                m = 12;
                y -= 1;
            }
        }

        m += p;
        if (m > 12) {
            if (m % 12 == 0) {
                y += (m / 12) - 1;
                m = 12;
            } else {
                y += (m / 12);
                m = (m % 12);
            }
        }

        return y + "." + two(m) + "." + two(d);
    }

    private String two(int x) {
        return (x < 10 ? "0" : "") + x;
    }
}