import java.util.Map;
import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> participants = new HashMap<>();
        
        for (String person : participant) {
            participants.putIfAbsent(person, 0);
            participants.put(person, participants.get(person) + 1);
        }
        
        for (String person : completion) {
            participants.put(person, participants.get(person) - 1);
            if (participants.get(person) == 0) {
                participants.remove(person);
            }
        }
        
        return participants.keySet().iterator().next();
    }
}