import java.util.*;

public class Solution {
    
    public static String[] solution(String[] record) {
        Map<String, String> users = new HashMap<>();
        List<String[]> events = new ArrayList<>();
        String[] txt = {"님이 들어왔습니다.", "님이 나갔습니다."};

        for (String r : record) {
            String[] tokens = r.split(" ");
            String event = tokens[0];

            if (event.equals("Enter")) {
                String uid = tokens[1];
                String nickname = tokens[2];
                events.add(new String[]{uid, "0"});
                users.put(uid, nickname);
            } else if (event.equals("Leave")) {
                String uid = tokens[1];
                events.add(new String[]{uid, "1"});
            } else {
                String uid = tokens[1];
                String nickname = tokens[2];
                users.put(uid, nickname);
            }
        }

        String[] answer = new String[events.size()];
        for (int i = 0; i < events.size(); i++) {
            String uid = events.get(i)[0];
            int type = Integer.parseInt(events.get(i)[1]);
            answer[i] = users.get(uid) + txt[type];
        }

        return answer;
    }
}